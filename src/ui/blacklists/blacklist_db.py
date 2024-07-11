from datetime import datetime

from PyQt5.QtWidgets import QTableWidget
from sqlalchemy import Boolean, Column, Integer, String

from ui.blacklists.constants import (
    BASE,
    COLUMN_ARTICLE_NAME,
    COLUMN_ARTICLE_NO,
    DB_TABLE_NAME_BLACKLISTS,
)
from ui.blacklists.utils import create_session, get_db_engine


# Definition der Tabelle
class Blacklists(BASE):
    __tablename__ = DB_TABLE_NAME_BLACKLISTS

    id = Column(Integer, primary_key=True, autoincrement=True)
    article_no = Column(String, nullable=False, unique=True, name=COLUMN_ARTICLE_NO)
    article_name = Column(String, nullable=False, name=COLUMN_ARTICLE_NAME)

    on_articles_bl = Column(Boolean, default=False)
    on_modules_bl = Column(Boolean, default=False)
    on_pv_inv_bl = Column(Boolean, default=False)
    on_bat_inv_bl = Column(Boolean, default=False)
    on_bat_bl = Column(Boolean, default=False)
    on_chg_point_bl = Column(Boolean, default=False)

    added_to_articles_bl = Column(String, nullable=True)
    added_to_modules_bl = Column(String, nullable=True)
    added_to_pv_inv_bl = Column(String, nullable=True)
    added_to_bat_inv_bl = Column(String, nullable=True)
    added_to_bat_bl = Column(String, nullable=True)
    added_to_chg_point_bl = Column(String, nullable=True)


def init_blacklists_db():
    ENGINE = get_db_engine()
    BASE.metadata.create_all(ENGINE)


def update_blacklist_db(
    self, article_no: str, article_name: str, table: QTableWidget, mode: str = "add"
) -> None:
    """
    Aktualisiert die Blacklists-Tabelle in der blacklist.db.

    :param article_no: Artikelnummer
    :param article_name: Artikelname
    :param table: QTableWidget
    :param mode: Modus ("add" oder "remove")
        "add" Fügt den Artikel zur DB-Tabelle hinzu, fals er noch nicht vorhanden ist. Falls doch, werden die Werte (*_val)
        in den Spalten entsprechend der Argumente "bl_bool_arg" und "bl_date_arg" bestimmt und gesetzt
        "remove": Der Artikel bleibt in der DB erhalten. Die Werte werden in den Spalten
        entsprechend der Argumente "bl_bool_arg" und "bl_date_arg" auf False (bl_bool_val) bzw. auf None (bl_date_val) gesetzt.

        Die Modus-Entscheidung erfolgt in einer Hilfsfunktion "set_val_by_mode(mode)"

    :return: None
    """

    bl_bool_arg = self.GENERAL_TABLE_MAP[table]["db_bl_bool"]
    bl_date_arg = self.GENERAL_TABLE_MAP[table]["db_added_to_bl_date"]

    Session = create_session()
    with Session() as session:
        # Überprüfen, ob article_no bereits in der Blacklists-Tabelle existiert
        existing_entry = (
            session.query(Blacklists).filter_by(article_no=article_no).first()
        )

        if existing_entry:

            bl_bool_val, bl_date_val = set_val_by_mode(self, mode, existing_entry)

            blacklist_change: dict = {
                bl_bool_arg: bl_bool_val,
                bl_date_arg: bl_date_val,
            }

            setattr(existing_entry, bl_bool_arg, bl_bool_val)
            setattr(existing_entry, bl_date_arg, bl_date_val)

            session.commit()

        else:
            new_blacklist_entry = Blacklists(
                article_no=article_no, article_name=article_name, **blacklist_change
            )
            session.add(new_blacklist_entry)
            session.commit()
    session.close()


def set_val_by_mode(self, mode, existing_entry):
    if mode == "add":
        bl_bool_val: bool = True
        bl_date_val: str = datetime.now().strftime("%Y-%m-%d - %H:%M:%S")

    elif mode == "remove":
        bl_bool_val: bool = False
        bl_date_val: str = None

        # Setzt auch die Werte in den allgemeinen Artikelspalten, da
        # die Blacklist-Werte für dieses Artikel gelöscht werden sollen.
        # Diese Änderungen werden in den allgemeinen Artikelspalten gespeichert.

        bl_bool_general: bool = self.GENERAL_TABLE_MAP[self.ui.articles_list][
            "db_bl_bool"
        ]
        bl_date_general: str = self.GENERAL_TABLE_MAP[self.ui.articles_list][
            "db_added_to_bl_date"
        ]

        setattr(existing_entry, bl_bool_general, False)
        setattr(existing_entry, bl_date_general, None)

    return bl_bool_val, bl_date_val

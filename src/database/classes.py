from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.constants import (
    BASE,
    COLUMN_ARTICLE_NAME,
    COLUMN_ARTICLE_NO,
    DB_TABLE_NAME_ART_SPECS,
    DB_TABLE_NAME_ARTICLES,
    DB_TABLE_NAME_BLACKLISTS,
)


def init_local_db() -> None:
    """
    Initialisiert eine lokale Datenbank in der Zusätzliche Informationen gespeichert werden können,
    welche durch den Nutzer der Software selbst angelegt und geupdated werden.
    Derzeit implementiert ist Speicherung von Artikeln und zusätzliche Informationen zu den Artikeln.
    Derzeit wird bezüglich der Artikel Folgendes in referenzierenden Tabellen gespeichert:
        - Listung auf Blacklisten , auf die Artikel durch den User gesetzt aber auch wieder entfernt werden können
        - Hinterlegung von technischen Kennzahlen eines Artikels, welche durch den Nutzer in Formularen eingetragen werden können
    """
    from database.utils import get_db_engine

    ENGINE = get_db_engine()
    BASE.metadata.create_all(ENGINE)


class Article(BASE):
    __tablename__ = DB_TABLE_NAME_ARTICLES
    id = Column(Integer, primary_key=True, autoincrement=True)
    article_no = Column(String, nullable=False, unique=True, name=COLUMN_ARTICLE_NO)
    article_name = Column(String, nullable=False, name=COLUMN_ARTICLE_NAME)


class Blacklists(BASE):
    __tablename__ = DB_TABLE_NAME_BLACKLISTS
    id = Column(Integer, primary_key=True)
    article_id = Column(
        Integer, ForeignKey(f"{DB_TABLE_NAME_ARTICLES}.id"), nullable=False
    )
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

    article = relationship("Article", backref=DB_TABLE_NAME_BLACKLISTS)


class ArticleSpecifications(BASE):
    __tablename__ = DB_TABLE_NAME_ART_SPECS
    id = Column(Integer, primary_key=True)
    article_id = Column(
        Integer, ForeignKey(f"{DB_TABLE_NAME_ARTICLES}.id"), nullable=False
    )
    module_power_kWp = Column(String, nullable=True)
    inv_power_kW = Column(String, nullable=True)
    bat_inv_power_kW = Column(String, nullable=True)
    coupling_type = Column(String, nullable=True)
    bat_capacity_kWh = Column(String, nullable=True)
    max_discharge_power_kW = Column(String, nullable=True)
    bat_technology_type = Column(String, nullable=True)

    article = relationship("Article", backref=DB_TABLE_NAME_ART_SPECS)

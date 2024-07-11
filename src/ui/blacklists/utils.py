import json
from configparser import ConfigParser
from typing import List, Tuple

import pandas as pd
from PyQt5.QtWidgets import QTableWidget
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from directories.constants import dir_paths
from ui.blacklists.constants import DB_TABLE_NAME_BLACKLISTS
from ui.blacklists.queries import get_query_for_articles_on_table


def is_on_blacklist(table_name, art_no, config):
    return config.has_section(table_name) and config.has_option(table_name, art_no)


def get_data_of_articles_from_bl(table: QTableWidget) -> List[Tuple[str, str, str]]:
    table_name = table.objectName()
    blacklist_path = dir_paths.dict["blacklist_path"]
    config = ConfigParser()
    config.read(blacklist_path)
    # Überprüfe, ob die angegebene Sektion vorhanden ist
    bl_articles: list = []
    data: str = ""
    if config.has_section(table_name):
        # Holen Sie sich alle Schlüssel-Wert-Paare in der Sektion

        bl_articles = [
            (
                str(json.loads(data)["article_no"]),
                str(json.loads(data)["article_name"]),
                str(json.loads(data)["date"]),
            )
            for _, data in config.items(table_name)
        ]

    return bl_articles


def get_bl_df_from_db(self, table: QTableWidget):

    bl_bool_arg = self.GENERAL_TABLE_MAP[table]["db_bl_bool"]
    bl_date_arg = self.GENERAL_TABLE_MAP[table]["db_added_to_bl_date"]
    db_table = DB_TABLE_NAME_BLACKLISTS

    # Definiere die SQL-Abfrage, um nur bestimmte Spalten auszuwählen
    engine = get_db_engine()
    query = get_query_for_articles_on_table(self, db_table, bl_bool_arg, bl_date_arg)
    # Lese die Tabelle direkt in einen DataFrame
    bl_df = pd.DataFrame()
    bl_df = pd.read_sql_query(query, con=engine)

    bl_df[bl_date_arg] = bl_df[bl_date_arg].fillna("Auf allgemeiner Blackliste")

    return bl_df


def get_db_engine():
    db_path: str = dir_paths.dict["blacklist_db_path"]
    engine = create_engine(f"sqlite:///{db_path}", echo=True)
    return engine


def create_session():
    ENGINE = get_db_engine()
    Session = sessionmaker(bind=ENGINE)
    return Session

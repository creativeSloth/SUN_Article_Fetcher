import json
from configparser import ConfigParser
from typing import List, Tuple

from sqlalchemy import create_engine

from directories.constants import dir_paths


def is_on_blacklist(table_name, art_no, config):
    return config.has_section(table_name) and config.has_option(table_name, art_no)


def get_db_engine():
    db_path: str = dir_paths.dict["blacklist_db_path"]
    engine = create_engine(f"sqlite:///{db_path}", echo=True)
    return engine


def get_data_of_articles_from_bl(table_name: str) -> List[Tuple[str, str, str]]:
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


def get_article_numbers_on_bl(table):

    table_name = table.objectName()
    # Laden Sie die Artikelnummern aus der Blacklist
    bl_article_nos = [
        article_no
        for article_no, _, _ in get_data_of_articles_from_bl(table_name=table_name)
    ]

    return bl_article_nos

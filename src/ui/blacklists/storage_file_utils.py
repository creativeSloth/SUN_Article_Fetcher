import json
from configparser import ConfigParser
from typing import List, Tuple

from PyQt5.QtWidgets import QTableWidget

from directories.constants import DB, DIRS


def is_on_blacklist(table_name, art_no, config):
    return config.has_section(table_name) and config.has_option(table_name, art_no)


def get_data_of_articles_from_bl(table: QTableWidget) -> List[Tuple[str, str, str]]:
    table_name = table.objectName()
    blacklist_path = DIRS.paths[DB]
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

import configparser
import json
import os
from datetime import datetime

from PyQt5.QtWidgets import QTableWidget

from directories.constants import dir_paths
from ui.blacklists.utils import is_on_blacklist


def remove_articles_from_bl(related_table: QTableWidget, article_no: str):
    table_name = related_table.objectName()
    blacklist_path = dir_paths.dict["blacklist_path"]

    config = configparser.ConfigParser()

    # Versuche, die Konfigurationsdatei zu lesen und den Eintrag zu entfernen
    config.read(blacklist_path)

    # Überprüfe, ob die angegebene Sektion und Option vorhanden sind
    if is_on_blacklist(table_name, article_no, config):
        config.remove_option(section=table_name, option=article_no)

        # Schreibe die aktualisierte Konfiguration in die Datei
        with open(blacklist_path, "w") as blacklist_file:
            config.write(blacklist_file)


def update_blacklist_file(
    article_no: str, article_name: str, table: QTableWidget
) -> None:
    table_name = table.objectName()
    blacklist_path = dir_paths.dict["blacklist_path"]

    blacklist = configparser.ConfigParser()

    # Lade vorhandene Konfiguration, wenn die Datei vorhanden ist
    if os.path.exists(blacklist_path):
        blacklist.read(blacklist_path)

    # Erstellen Sie die Sektion, wenn sie noch nicht existiert
    if not blacklist.has_section(table_name):
        blacklist.add_section(table_name)

    # Überprüfen, ob Artikel bereits vorhanden sind, und nur neue hinzufügen
    existing_articles = set(blacklist.options(table_name))

    date = datetime.now().strftime("%Y-%m-%d - %H:%M:%S")
    data = json.dumps(
        {"article_no": article_no, "article_name": article_name, "date": date}
    )
    if article_no not in existing_articles:
        # Fügen Sie die Daten als Optionen unter der gegebenen Sektion hinzu
        blacklist.set(table_name, article_no, data)

    # Schreibe die aktualisierte Konfiguration in die Datei
    with open(blacklist_path, "w") as blacklist_file:
        blacklist.write(blacklist_file)

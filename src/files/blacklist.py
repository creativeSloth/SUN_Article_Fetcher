import configparser
import os

import pandas as pd
from PyQt5 import QtWidgets
from qtpy import QtWidgets

from directories.directory_base import dir_paths
from files.utils import is_on_blacklist
from styles.styles_Handler import initialize_ui_style
from ui.buttons.button_lists import add_btns_into_table_cells
from ui.buttons.custom_button import customize_push_buttons
from ui.tables.utils import (
    clear_table,
    disable_colums_edit,
    remove_row_with_button_from_table,
    resize_columns_to_contents,
)
from ui.windows import blacklistWindow


class Blacklist(QtWidgets.QDialog):
    def __init__(self, table_name, table_name_ger, parent=None):
        super().__init__(parent)
        self.ui = blacklistWindow.Ui_blacklist_dialog()
        self.ui.setupUi(self)

        self.table_name = table_name

        self.setWindowTitle(table_name_ger)

        self.initialize()
        # Verbinde die Signale mit den entsprechenden Slots
        self.map_ui_buttons()

    def initialize(self):
        initialize_ui_style(self)
        # connect_table_buttons(self)

    def map_ui_buttons(self):
        from ui.tables.tables_base import connect_sort_indicator_changed

        connect_sort_indicator_changed(self)


BLACKLISTS = []
BLACKLISTS_TABLE_MAP = []


def get_blacklist_map(self):

    button_dict = {
        "PV_modules_list": (self.ui.open_PV_modules_blacklist, "PV-Module"),
        "PV_inverters_list": (self.ui.open_PV_inverters_blacklist, "PV-Wechselrichter"),
        "BAT_inverters_list": (
            self.ui.open_BAT_inverters_blacklist,
            "Batterie-Wechselrichter",
        ),
        "BAT_storage_list": (self.ui.open_BAT_storage_blacklist, "Batterie-Speicher"),
        "CHG_point_list": (self.ui.open_CHG_point_blacklist, "Ladestation"),
        "articles_list": (self.ui.open_articles_blacklist, "Allgemeine Artikel"),
    }

    return button_dict


def initialize_blacklist_dialogs(self):
    tables_dict = get_blacklist_map(self)

    for key, value in tables_dict.items():
        table_name, table_name_ger = key, value[1]
        table_name_ger = f"{table_name_ger} - Blacklist"

        # Erstelle dynamisch ein Attribut für jede Tabelle
        setattr(
            self,
            f"{table_name}_blacklist_dlg",
            Blacklist(table_name=table_name, table_name_ger=table_name_ger),
        )

        dialog_instance: Blacklist = getattr(self, f"{table_name}_blacklist_dlg", None)

        dialog_instance.setObjectName(f"{table_name}")

        BLACKLISTS_TABLE_MAP.append(
            (dialog_instance.ui.blacklist, dialog_instance.ui.verticalLayout)
        )
        BLACKLISTS.append(dialog_instance)


def init_blacklist_button_click_signal(self, table: QtWidgets.QTableWidget):
    table_name = table.objectName()
    button = get_blacklist_map(self)[table_name][0]
    if button:
        button.clicked.connect(
            lambda: on_blacklist_button_click(self, device_table=table)
        )


def on_blacklist_button_click(self, device_table: QtWidgets.QTableWidget) -> None:

    device_table_name: str = device_table.objectName()

    # Zugriff auf die entsprechende Instanz des Blacklist-Dialogs
    dialog_instance: Blacklist = getattr(
        self, f"{device_table_name}_blacklist_dlg", None
    )
    blacklist_table: QtWidgets.QTableWidget = dialog_instance.ui.blacklist
    clear_table(blacklist_table)

    # Überprüfe, ob die Instanz existiert, bevor du die Methode aufrufst
    if dialog_instance is not None:
        dialog_instance.show()

    from ui.tables.tables_base import fill_bl_tables

    fill_bl_tables(self, device_table_name=device_table_name, table=blacklist_table)
    add_btns_into_table_cells(
        dialog_instance,
        table=blacklist_table,
        column=3,
        button_type="move_from_bl",
        on_button_pressed=on_remove_articles_from_ui_bl,
    )

    customize_push_buttons(self)

    resize_columns_to_contents(blacklist_table)
    disable_colums_edit(blacklist_table)


def on_remove_articles_from_ui_bl(
    bl_table: QtWidgets.QTableWidget = None, push_button: QtWidgets.QPushButton = None
):
    device_table = bl_table.parent()
    while device_table.parent():
        device_table = device_table.parent()

    device_table_name = device_table.objectName()

    removed, article_no, _ = remove_row_with_button_from_table(
        table=bl_table, push_button=push_button
    )

    if removed:
        remove_articles_from_blacklist(table_name=device_table_name, art_no=article_no)


def remove_articles_from_blacklist(table_name: str, art_no: str):
    blacklist_path = dir_paths.dict["blacklist_path"]

    config = configparser.ConfigParser()

    # Versuche, die Konfigurationsdatei zu lesen und den Eintrag zu entfernen
    config.read(blacklist_path)

    # Überprüfe, ob die angegebene Sektion und Option vorhanden sind
    if is_on_blacklist(table_name, art_no, config):
        config.remove_option(section=table_name, option=art_no)

        # Schreibe die aktualisierte Konfiguration in die Datei
        with open(blacklist_path, "w") as blacklist_file:
            config.write(blacklist_file)


def update_blacklist(df: pd.DataFrame, table_name: str):
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
    for _, row in df.iterrows():
        article_no = row["article_no"]
        article_name = row["article_name"]
        if article_no not in existing_articles:
            # Fügen Sie die Daten als Optionen unter der gegebenen Sektion hinzu
            blacklist.set(table_name, article_no, article_name)

    # Schreibe die aktualisierte Konfiguration in die Datei
    with open(blacklist_path, "w") as blacklist_file:
        blacklist.write(blacklist_file)


def read_blacklist_articles(table_name: str):
    blacklist_path = dir_paths.dict["blacklist_path"]
    config = configparser.ConfigParser()
    config.read(blacklist_path)
    # Überprüfe, ob die angegebene Sektion vorhanden ist
    bl_articles = []
    if config.has_section(table_name):
        # Holen Sie sich alle Schlüssel-Wert-Paare in der Sektion
        bl_articles = [
            (str(number), str(value)) for number, value in config.items(table_name)
        ]

    return bl_articles

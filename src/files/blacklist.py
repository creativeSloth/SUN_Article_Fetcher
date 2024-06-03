from PyQt5 import QtWidgets
from styles.styles_Handler import init_ui
from ui import blacklistWindow
import configparser
import os

import directories.directory_base as directory_base

from qtpy import QtWidgets

from directories import directory_base
from tables.tables_base import import_from_df_row, clear_table, resize_columns_to_contents, disable_colums_edit


BLACKLISTS_TABLE_MAP = []


class Blacklist(QtWidgets.QDialog):
    def __init__(self, table_name, table_name_ger,
                 parent=None):
        super().__init__(parent)
        self.ui = blacklistWindow.Ui_blacklist_dialog()
        self.ui.setupUi(self)

        self.table_name = table_name

        self.setWindowTitle(table_name_ger)

        self.initialize()
        # Verbinde die Signale mit den entsprechenden Slots
        self.map_ui_buttons()

    def initialize(self):
        init_ui(self)
        # connect_table_buttons(self)

    def map_ui_buttons(self):
        pass


def get_blacklist_map(self):

    button_dict = {
        'PV_modules_list': (self.ui.open_PV_modules_blacklist, 'PV-Module'),
        'PV_inverters_list': (self.ui.open_PV_inverters_blacklist, 'PV-Wechselrichter'),
        'BAT_inverters_list': (self.ui.open_BAT_inverters_blacklist, 'Batterie-Wechselrichter'),
        'BAT_storage_list': (self.ui.open_BAT_storage_blacklist, 'Batterie-Speicher'),
        'CHG_point_list': (self.ui.open_CHG_point_blacklist, 'Ladestation')
    }

    return button_dict


def initialize_blacklist_dialogs(self):
    tables_dict = get_blacklist_map(self)

    for key, value in tables_dict.items():
        table_name, table_name_ger = key, value[1]
        table_name_ger = f"{table_name_ger} - Blacklist"

        # Erstelle dynamisch ein Attribut für jede Tabelle
        setattr(self, f"{table_name}_blacklist_dlg", Blacklist(
            table_name, table_name_ger))
        dialog_instance: Blacklist = getattr(
            self, f"{table_name}_blacklist_dlg", None)
        BLACKLISTS_TABLE_MAP.append((dialog_instance.ui.blacklist,
                                     dialog_instance.ui.verticalLayout))


def init_blacklist_button_click_signal(self, table):
    table_name = table.objectName()
    button = get_blacklist_map(self)[table_name][0]
    if button:
        button.clicked.connect(
            lambda: on_blacklist_button_click(self, table=table))


def on_blacklist_button_click(self, table):

    table_name = table.objectName()
    # Zugriff auf die entsprechende Instanz des Blacklist-Dialogs
    dialog_instance: Blacklist = getattr(
        self, f"{table_name}_blacklist_dlg", None)
    bl_table: QtWidgets.QTableWidget = dialog_instance.ui.blacklist
    clear_table(bl_table)

    # Überprüfe, ob die Instanz existiert, bevor du die Methode aufrufst
    if dialog_instance is not None:
        dialog_instance.show()

    bl_articles = read_blacklist_articles(table_name=table_name)

    # Zum Sicherstellen dass bl__articles eine Instanz von List ist und ein Element hat
    if isinstance(bl_articles, list) and bl_articles:
        for article in bl_articles:
            # Import data from each row of the blacklist articles
            import_from_df_row(bl_table, data_row=article,
                               import_column_count=2)
    place_button_into_cell(self, table_name, bl_table, 3, "[X]")
    resize_columns_to_contents(bl_table)
    disable_colums_edit(bl_table)


def place_button_into_cell(self, table_name: str, bl_table: QtWidgets.QTableWidget, column: int, text: str = ""):

    row_count = bl_table.rowCount()
    for row in range(row_count):
        # Erstelle dynamisch ein Attribut für jede Tabelle
        setattr(self, f"push_button_{row}", QtWidgets.QPushButton(text))
        push_button = getattr(self, f"push_button_{row}", None)
        push_button.setFixedSize(50, 25)

        push_button.clicked.connect(
            lambda _, table_name=table_name, bl_table=bl_table, push_button=push_button: remove_articles_from_ui_bl(
                table_name=table_name, bl_table=bl_table, push_button=push_button))
        bl_table.setCellWidget(row, column, push_button)


def remove_articles_from_ui_bl(table_name: str, bl_table: QtWidgets.QTableWidget = None, push_button: QtWidgets.QPushButton = None):
    if push_button is not None and bl_table is not None:
        index = bl_table.indexAt(push_button.pos())
        if index.isValid():
            row = index.row()
            art_no = bl_table.item(row, 1).text()
            remove_articles_from_blacklist(table_name=table_name,
                                           art_no=art_no)

            bl_table.removeRow(row)


def remove_articles_from_blacklist(table_name, art_no: str):
    blacklist_path = directory_base.MAIN_PATHS.dict['blacklist_path']
    config = configparser.ConfigParser()

    # Versuche, die Konfigurationsdatei zu lesen und den Eintrag zu entfernen
    config.read(blacklist_path)
    # Überprüfe, ob die angegebene Sektion und Option vorhanden sind
    if config.has_section(table_name) and config.has_option(table_name, art_no):
        config.remove_option(table_name, art_no)

        # Schreibe die aktualisierte Konfiguration in die Datei
        with open(blacklist_path, 'w') as blacklist_file:
            config.write(blacklist_file)


def update_blacklist(df, table_name):
    blacklist_path = directory_base.MAIN_PATHS.dict['blacklist_path']

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
        article_no = row['article_no']
        article_name = row['article_name']
        if article_no not in existing_articles:
            # Fügen Sie die Daten als Optionen unter der gegebenen Sektion hinzu
            blacklist.set(table_name, article_no, article_name)

    # Schreibe die aktualisierte Konfiguration in die Datei
    with open(blacklist_path, 'w') as blacklist_file:
        blacklist.write(blacklist_file)


def read_blacklist_articles(table_name):
    blacklist_path = directory_base.MAIN_PATHS.dict['blacklist_path']
    config = configparser.ConfigParser()
    config.read(blacklist_path)
    # Überprüfe, ob die angegebene Sektion vorhanden ist
    bl_articles = []
    if config.has_section(table_name):
        # Holen Sie sich alle Schlüssel-Wert-Paare in der Sektion
        bl_articles = [(str(number), str(value))
                       for number, value in config.items(table_name)]

    return bl_articles

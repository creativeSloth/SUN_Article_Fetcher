import configparser
import os

import directories.directory_base as directory_base

from qtpy import QtWidgets

from directories import directory_base
from tables.tables_base import import_from_df_row
from ui import blacklistWindow
from styles.styles_Handler import init_ui


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


def init_blacklist_button_click_signal(self, table):
    table_name = table.objectName()
    button = get_blacklist_map(self)[table_name][0]
    if button:
        button.clicked.connect(
            lambda: on_blacklist_button_click(self, table=table))


def on_blacklist_button_click(self, table):
    table_name = table.objectName()
    # Zugriff auf die entsprechende Instanz des Blacklist-Dialogs
    dialog_instance = getattr(self, f"{table_name}_blacklist_dlg", None)
    bl_table = dialog_instance.ui.blacklist

    # Überprüfe, ob die Instanz existiert, bevor du die Methode aufrufst
    if dialog_instance is not None:
        dialog_instance.show()

    bl_articles = read_blacklist_articles(table_name=table_name)

    # Zum SIcherstellen dass bl__articles eine Instanz von List ist und ein Element hat
    if isinstance(bl_articles, list) and bl_articles:
        for article in bl_articles:
            # Import data from each row of the blacklist articles
            import_from_df_row(bl_table, df_row=article, import_column_count=2)


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

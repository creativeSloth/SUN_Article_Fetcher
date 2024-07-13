from pandas import DataFrame
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidget

from database.constants import COLUMN_ARTICLE_NAME, COLUMN_ARTICLE_NO
from database.queries import get_bl_df_from_db
from ui.blacklists.gui_window import init_blacklist_button_click_signal
from ui.buttons.button_lists import add_btns_into_table_cells
from ui.buttons.custom_button import customize_push_buttons
from ui.tables.data_content_helper import (
    fill_device_specs_in_device_tables,
    mark_documents_availability,
    put_non_bl_articles_on_table,
)
from ui.tables.decorators import customize_table_row
from ui.tables.search_bar import (
    add_table_header_search_box,
    init_search_button_click_signal,
)
from ui.tables.utils import (
    clear_table,
    disable_colums_edit,
    get_all_tables_to_layout_map,
    remove_article_from_table_row,
    resize_columns_to_contents,
    table_name_and_count_are_valid,
)
from ui.text_edits.ui_fields_base import get_all_mainwindow_tables, get_device_tables

# from ui.blacklists.storage_file_utils import get_data_of_articles_from_bl


def initialize_table_search(self):
    # Hole die Artikeltabelle und ihr Layout
    GENERAL_TABLE_MAP = get_all_tables_to_layout_map(self)

    # Iteriere durch alle Tabellen in der allgemeinen Tabellen-Map
    for item in GENERAL_TABLE_MAP:
        table: QtWidgets.QTableWidget
        layout: QtWidgets.QLayout
        table, layout = item

        # Füge ein Suchfeld zum Tabellenkopf hinzu

        button, text_edit = add_table_header_search_box(
            self, table=table, layout=layout
        )

        # Initialisiere das Signal für den Suchbutton-Klick
        init_search_button_click_signal(table=table, button=button, text_edit=text_edit)

        # ? methode passt nicht so richtig hier her
        # Falls die Tabelle eine Gerätetabelle ist, initialisiere das Signal für den Blacklist-Button-Klick
        if table in get_all_mainwindow_tables(self):
            init_blacklist_button_click_signal(self, table=table)


@customize_table_row
def fill_article_table(self, table: QtWidgets.QTableWidget, df: DataFrame = None):

    put_non_bl_articles_on_table(self, table, df, import_column_count=3)
    mark_documents_availability(self, table)
    add_btns_into_table_cells(
        self,
        table,
        column=table.columnCount() - 1,
        button_type="move_to_bl",
        on_button_pressed=remove_article_from_table_row,
    )
    customize_push_buttons(self)
    resize_columns_to_contents(table=table)
    disable_colums_edit(table, firstcol=1, lastcol=4)


def fill_device_lists(self, df):
    tables = get_device_tables(self)
    for table in tables:
        fill_specific_device_list(self, table=table, df=df)

    QtWidgets.QMessageBox.information(
        self, "Abgeschlossen!", "Geräteliste wurden geladen!"
    )


@customize_table_row
def fill_specific_device_list(self, table: QtWidgets.QTableWidget, df: DataFrame):

    put_non_bl_articles_on_table(self, table, df, import_column_count=4)
    add_btns_into_table_cells(
        self,
        table,
        column=table.columnCount() - 1,
        button_type="move_to_bl",
        on_button_pressed=remove_article_from_table_row,
    )
    customize_push_buttons(self)
    fill_device_specs_in_device_tables(table)
    resize_columns_to_contents(table=table)
    disable_colums_edit(table, firstcol=1, lastcol=5)


def adding_specific_columns(self, table, tw_row=None, df_row=None):
    if table == self.ui.PV_modules_list:
        # Spalte 6 (dynamisch) mit den Werten aus der Spalte 4 des DataFrames
        table.setItem(tw_row, 5, QtWidgets.QTableWidgetItem(""))

    if table == self.ui.PV_inverters_list:
        # Spalte 6 (dynamisch) mit den Werten aus der Spalte 4 des DataFrames
        table.setItem(tw_row, 5, QtWidgets.QTableWidgetItem(""))

    if table == self.ui.BAT_inverters_list:
        # Spalte 6 (dynamisch) mit den Werten aus der Spalte 4 des DataFrames
        table.setItem(tw_row, 5, QtWidgets.QTableWidgetItem(""))
        # Spalte 7 (dynamisch) mit den Werten aus der Spalte 5 des DataFrames
        table.setItem(tw_row, 6, QtWidgets.QTableWidgetItem(""))

    if table == self.ui.BAT_storage_list:
        # Spalte 6 (dynamisch) mit den Werten aus der Spalte 4 des DataFrames
        table.setItem(tw_row, 5, QtWidgets.QTableWidgetItem(""))
        # Spalte 7 (dynamisch) mit den Werten aus der Spalte 5 des DataFrames
        table.setItem(tw_row, 6, QtWidgets.QTableWidgetItem(""))
        # Spalte 8 (dynamisch) mit den Werten aus der Spalte 6 des DataFrames
        table.setItem(tw_row, 7, QtWidgets.QTableWidgetItem(""))
        # Spalte 9 (dynamisch) mit den Werten aus der Spalte 7 des DataFrames
        table.setItem(tw_row, 8, QtWidgets.QTableWidgetItem(""))

    if table == self.ui.CHG_point_list:
        pass


@customize_table_row
def fill_bl_tables(
    self, device_table: QTableWidget, table: QtWidgets.QTableWidget
) -> None:
    from ui.tables.utils import import_from_df_row

    bl_df = get_bl_df_from_db(self, device_table)
    bl_df_selected: DataFrame = bl_df[
        [
            COLUMN_ARTICLE_NO,
            COLUMN_ARTICLE_NAME,
            self.GENERAL_TABLE_MAP[device_table]["db_added_to_bl_date"],
        ]
    ]

    # Zum Sicherstellen dass bl_articles eine Instanz von List ist und ein Element hat
    if isinstance(bl_df_selected, DataFrame):
        for _, data in bl_df_selected.iterrows():
            # Import data from each row of the blacklist articles
            import_from_df_row(table, data_row=data, import_column_count=3)


def fill_tables_content(self, saved_tables_content: dict):
    """
    Diese Funktion füllt die gespeicherten Inhalte der Qt-Tabellen.
    Es wird verwendet, um vorher gespeicherte Inhalte wiederherzustellen.
    Args:
        saved_tables_content (dict): Ein Dictionary, das die gespeicherten Inhalte enthält.
        Keys sind Strings, die den Namen der gespeicherten Qt-Tabelle enthalten,
        und Values sind DataFrames, die die gespeicherten Inhalte enthalten.




    """

    # Alle Tabellen holen
    tables = get_all_mainwindow_tables(self)
    for table in tables:
        clear_table(table)

    # Durch jedes Element im gespeicherten Tabelleninhalt iterieren
    for table_map, value in saved_tables_content.items():
        # Tabellennamen, Zeile und Spalte extrahieren
        table_name = table_map.split("(")[0]
        table_row = int(table_map.split("(")[1].split(";")[0])
        table_column = int(table_map.split("(")[1].split(";")[1].split(")")[0])

        # Durch jede Qt-Tabelle iterieren
        for table in tables:

            # Wenn der Tabellenname übereinstimmt - Wenn die Anzahl der Zeilen kleiner oder gleich der Zielzeile ist
            if table_name_and_count_are_valid(table, table_name, table_row):

                # Differenz berechnen und fehlende Zeilen einfügen
                diff = table_row - table.rowCount()
                for _ in range(diff + 1):
                    table.insertRow(table.rowCount())

                # Checkbox in Spalte 1 setzen
                checkbox_item = QtWidgets.QTableWidgetItem()
                checkbox_item.setFlags(
                    QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled
                )
                checkbox_item.setCheckState(QtCore.Qt.Checked)

                # Checkbox in die Tabelle einfügen
                table.setItem(table_row, 0, checkbox_item)

                # Wert in die spezifische Spalte einfügen
                # Hier wird der Wert in ein QTableWidgetItem-Objekt konvertiert
                value_item = QtWidgets.QTableWidgetItem(str(value))
                table.setItem(table_row, table_column, value_item)

from pandas import DataFrame
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidget

from ui.tables.data_content_helper import (
    bl_art_to_bl,
    dev_specs_to_table,
    none_bl_art_to_table,
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
    resize_columns_to_contents,
    table_name_and_count_are_valid,
)
from ui.text_edits.ui_fields_base import get_all_mainwindow_tables, get_device_tables


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
        init_search_button_click_signal(
            self, table=table, button=button, text_edit=text_edit
        )


def fill_article_table(self, table: QTableWidget, df: DataFrame = None):

    none_bl_art_to_table(self, table=table, df=df, import_column_count=3)
    resize_columns_to_contents(table=table)
    disable_colums_edit(table, firstcol=1, lastcol=4)
    QtWidgets.QMessageBox.information(
        self, "Abgeschlossen!", "Artikelliste wurden geladen!"
    )


def fill_device_tables(self, df: DataFrame = None):
    tables = get_device_tables(self)
    for table in tables:
        fill_specific_device_list(self, table=table, df=df)

    QtWidgets.QMessageBox.information(
        self, "Abgeschlossen!", "Geräteliste wurden geladen!"
    )


def fill_specific_device_list(self, table: QTableWidget, df: DataFrame) -> None:
    """
    Füllt die Geräteigenschaften aus den in der Datenbank hinterlegten Werten in die entsprechende Zelle des QTableWidgets.
    ________________________________________________________________________________________________________________________________
    :param table: QTableWidget, in der die Gerätespezifikationen geladen werden sollen
    :param df : DataFrame, aus dem die Artikel geladen werden sollen
    :return: None
    ________________________________________________________________________________________________________________________________
    """

    none_bl_art_to_table(self, table=table, df=df, import_column_count=4)
    dev_specs_to_table(table)
    resize_columns_to_contents(table=table)
    disable_colums_edit(table, firstcol=1, lastcol=5)


def adding_specific_columns(self, table: QTableWidget, tw_row=None, df_row=None):
    """
    Fügt spezielle Spalten hinzu, je nach der Art der Gerätetabelle
    :param table: Gerätetabelle
    :param tw_row: Zeile der Gerätetabelle
    :param df_row: Zeile des DataFrames
    :return: None
    """
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
def fill_bl_tables(self, bl_table: QTableWidget) -> None:
    """
    Füllt die Qt-Tabellen mit den Blacklist-Artikeln.
    :param table: Die Qt-Tabelle, in der die Blacklist-Artikel gefüllt werden sollen.
    :return: None"""

    bl_art_to_bl(self, bl_table)
    resize_columns_to_contents(bl_table)
    disable_colums_edit(bl_table)


def fill_tables_content(self, saved_tables_content: dict) -> None:
    """
    Diese Funktion füllt die gespeicherten Inhalte der Qt-Tabellen.
    Es wird verwendet, um vorher gespeicherte Inhalte wiederherzustellen.
    :param saved_tables_content:
    Ein Dictionary, das die gespeicherten Inhalte enthält.
    :return: None"""

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

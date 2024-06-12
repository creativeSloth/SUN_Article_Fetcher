from PyQt5 import QtWidgets
from qtpy import QtCore, QtWidgets

import files.blacklist as blacklist
from ui.fields.ui_fields_base import get_articles_table, get_device_tables
from ui.tables.customize_row import customize_table_row


def get_fixed_val_columns():
    discard_columns = ["<>", "Menge verbraucht [Stk.]", "Seriennummer", "Artikelnummer"]
    return discard_columns


def get_all_tables_to_layout_map(self):
    article_table = get_articles_table(self)
    article_table_layout = self.ui.verticalLayout
    ARTICLES_TABLE_MAP = [(table, article_table_layout) for table in article_table]
    # Hole die Gerätetabellen und ihr Layout
    device_tables = get_device_tables(self)
    device_table_layout = self.ui.verticalLayout_3
    DEVICE_TABLE_MAP = [(table, device_table_layout) for table in device_tables]
    # Kombiniere die Artikeltabelle, Gerätetabellen und die Blacklist-Tabellen
    GENERAL_TABLE_MAP = (
        ARTICLES_TABLE_MAP + DEVICE_TABLE_MAP + blacklist.BLACKLISTS_TABLE_MAP
    )

    return device_tables, GENERAL_TABLE_MAP


def clear_table(table: QtWidgets.QTableWidget):
    # Setze die Anzahl der Zeilen auf 0, um alle Zeilen zu entfernen
    table.setRowCount(0)


def resize_columns_to_contents(table):
    columns = table.columnCount()
    header = table.horizontalHeader()
    for i in range(columns):
        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)


def get_column_index(table, column):
    """Suche den Index der 'Artikelnummer'-Spalte in der Tabelle."""
    column_index = None
    for column_index in range(table.columnCount()):
        if table.horizontalHeaderItem(column_index).text() == column:
            return column_index
    return None


def disable_colums_edit(table: QtWidgets.QTableWidget, firstcol=0, lastcol: int = None):
    if lastcol is None:
        lastcol = table.columnCount()

    for row in range(table.rowCount()):
        for col in range(firstcol, lastcol):
            # Das vorhandene QTableWidgetItem abrufen
            item = table.item(row, col)
            # Entfernt das Bearbeitungsflag für die Zelle
            if item is not None:
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)


@customize_table_row
def on_sort_indicator_changed(self, table):
    pass


def table_name_and_count_are_valid(table, table_name, table_row):
    return table_name == table.objectName().lower() and table.rowCount() <= table_row


def remove_row_with_button_from_table(
    table: QtWidgets.QTableWidget, push_button: QtWidgets.QPushButton
):
    if push_button is not None and table is not None:
        index = table.indexAt(push_button.pos())
        if index.isValid():
            row = index.row()
            article_no = table.item(row, 1).text()
            article_name = table.item(row, 1).text()
            table.removeRow(row)
            removed: bool = True
    return removed, article_no, article_name


def is_not_on_bl(blacklist_article_numbers, df_row):
    return str(df_row.iloc[0]) not in blacklist_article_numbers


def check_article_number_on_bl(table):
    from files.blacklist import read_blacklist_articles

    table_name = table.objectName()
    # Laden Sie die Artikelnummern aus der Blacklist
    blacklist_article_numbers = [
        number for number, _ in read_blacklist_articles(table_name=table_name)
    ]

    return blacklist_article_numbers

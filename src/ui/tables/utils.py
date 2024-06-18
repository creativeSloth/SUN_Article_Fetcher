import pandas as pd
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QHeaderView,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)

import files.blacklist as blacklist
from ui.buttons.utils import create_and_set_obj_property
from ui.fields.ui_fields_base import get_articles_table, get_device_tables
from ui.tables.table_decorators import customize_table_row


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

    return GENERAL_TABLE_MAP


def clear_table(table: QTableWidget):
    # Setze die Anzahl der Zeilen auf 0, um alle Zeilen zu entfernen
    table.setRowCount(0)


def resize_columns_to_contents(table):
    columns = table.columnCount()
    header = table.horizontalHeader()
    for i in range(columns):
        header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(i, QHeaderView.Interactive)


def get_column_index(table, column):
    """Suche den Index der 'Artikelnummer'-Spalte in der Tabelle."""
    column_index = None
    for column_index in range(table.columnCount()):
        if table.horizontalHeaderItem(column_index).text() == column:
            return column_index
    return None


def disable_colums_edit(table: QTableWidget, firstcol=0, lastcol: int = None):
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


def remove_row_with_button_from_table(table: QTableWidget, push_button: QPushButton):
    removed: bool = False
    article_no: str = ""
    article_name: str = ""

    if push_button is not None and table is not None:
        parent = push_button.parent()
        while parent is not None:
            if (
                isinstance(parent, QWidget)
                and getattr(parent, "cell_widget", None) == "contains_push_button"
            ):
                break
            parent = parent.parent()

        index = table.indexAt(parent.pos())
        if index.isValid():
            row = index.row()
            article_no = table.item(row, 1).text()
            article_name = table.item(row, 2).text()
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


def remove_article_from_table_row(
    table: QTableWidget = None, push_button: QPushButton = None
):
    from files.blacklist import update_blacklist

    removed, article_no, article_name = remove_row_with_button_from_table(
        table, push_button
    )

    if removed:
        # Holen Sie sich alle ausgewählten Dateien im Table Widget
        df = pd.DataFrame(columns=["article_no", "article_name"])

        new_data = pd.DataFrame(
            {"article_no": [article_no], "article_name": [article_name]}
        )
        # Füge die neuen Daten zum vorhandenen DataFrame hinzu
        df = pd.concat([df, new_data], ignore_index=True)

        update_blacklist(df, table.objectName())


def import_from_df_row(
    table: QTableWidget,
    data_row,
    import_column_count: int = None,
) -> None:
    """Importiert eine Zeile aus einem Datensatz, der Datensatz kann ein DataFrame oder ein Tuple sein

    Args:
        table (QtWidgets.QTableWidget): Die Tabelle die den Datensatz aufnehmen soll
        data_row (pd.Series | tuple): Eine Datenzeile, deren Datensätze in eine jeweilige Spalte eingefügt werden soll.
        Hier soll die 0 Spalte der Tabelle für eine Checkbox, übersprungen werden
        import_column_count (int, optional): Die Anzahl der Spalten in die eingefügt werden soll.
    """

    tw_row = table.rowCount()
    table.insertRow(tw_row)

    # Spalte 0 (statisch) mit einer Checkbox

    checkbox = QCheckBox()
    checkbox.setChecked(True)
    checkbox.setObjectName(f"CheckBox_{table.objectName()}_{tw_row}_0")

    layout = QHBoxLayout()
    layout.setObjectName(f"Layout_{table.objectName()}_{tw_row}_0")
    layout.setContentsMargins(7, 2, 7, 2)
    layout.setSpacing(2)

    cell_widget = QWidget()
    cell_widget.setLayout(layout)
    create_and_set_obj_property(
        obj=cell_widget,
        property_type="cell_widget",
        property_value="contains_checkbox",
    )

    layout.addWidget(checkbox)

    # Spalte 1 mit der CheckBox
    table.setCellWidget(tw_row, 0, cell_widget)

    for index in range(import_column_count):

        # Überprüfe die Anzahl der Spalten in data_row
        col_count_data_row = len(data_row)
        if col_count_data_row > index:
            if isinstance(data_row, pd.Series) and data_row.iloc[index] is not None:
                item_col = QTableWidgetItem(str(data_row.iloc[index]))
                table.setItem(tw_row, index + 1, item_col)
            elif isinstance(data_row, tuple) and data_row[index] is not None:
                item_col = QTableWidgetItem(str(data_row[index]))
                table.setItem(tw_row, index + 1, item_col)


#! Ungenutzt   ####################################################################################################################


def remove_articles_from_table(table):
    from files.blacklist import update_blacklist

    # Holen Sie sich alle ausgewählten Dateien im Table Widget
    df = pd.DataFrame(columns=["article_no", "article_name"])
    rows_to_remove = []
    for row in range(table.rowCount()):
        checkbox_item = table.item(row, 0)
        article_no = table.item(row, 1).text()
        article_name = table.item(row, 2).text()

        # Überprüfe, ob die Checkbox in der aktuellen Zeile angehakt ist
        if checkbox_item and checkbox_item.checkState() == QtCore.Qt.Checked:

            new_data = pd.DataFrame(
                {"article_no": [article_no], "article_name": [article_name]}
            )
            # Füge die neuen Daten zum vorhandenen DataFrame hinzu
            df = pd.concat([df, new_data], ignore_index=True)
            rows_to_remove.append(row)
    # Entfernen Sie die ausgewählten Zeilen
    for row in reversed(rows_to_remove):
        table.removeRow(row)

    update_blacklist(df, table.objectName())


#! ##############################################################################################################################

import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton, QTableWidget

from blacklist.blacklist_gui import (
    get_article_numbers_on_bl,
    get_data_of_articles_from_bl,
    init_blacklist_button_click_signal,
)
from files import logs_and_config
from files.sys_files import get_files_in_source_path, get_paths
from ui.buttons.button_lists import add_btns_into_table_cells, add_doc_avlbl_btns
from ui.buttons.custom_button import customize_push_buttons
from ui.tables.search_bar import (
    add_table_header_search_box,
    init_search_button_click_signal,
)
from ui.tables.table_decorators import customize_table_row
from ui.tables.utils import (
    clear_table,
    disable_colums_edit,
    get_all_tables_to_layout_map,
    get_column_index,
    get_fixed_val_columns,
    import_from_df_row,
    is_not_on_bl,
    remove_row_with_button_from_table,
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
        init_search_button_click_signal(table=table, button=button, text_edit=text_edit)

        # ? methode passt nicht so richtig hier her
        # Falls die Tabelle eine Gerätetabelle ist, initialisiere das Signal für den Blacklist-Button-Klick
        if table in get_all_mainwindow_tables(self):
            init_blacklist_button_click_signal(self, table=table)


@customize_table_row
def fill_article_table(self, table: QtWidgets.QTableWidget, df: pd.DataFrame = None):
    put_non_bl_articles_on_table(table, df, import_column_count=3)
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


def put_non_bl_articles_on_table(
    table: QtWidgets.QTableWidget, df: pd.DataFrame, import_column_count: int = 0
):
    clear_table(table=table)

    blacklist_article_numbers = get_article_numbers_on_bl(table)
    if df is not None:
        for _, df_row in df.iterrows():
            # Überprüfen Sie, ob die Artikelnummer nicht in der Blacklist enthalten ist
            if is_not_on_bl(blacklist_article_numbers, df_row):
                import_from_df_row(
                    table, data_row=df_row, import_column_count=import_column_count
                )


def mark_documents_availability(self, table: QTableWidget):

    source_path, _, _ = get_paths()
    all_files = get_files_in_source_path(self, source_path)
    add_doc_avlbl_btns(
        self,
        table=table,
        column=0,
        button_type="doc_available",
        all_files=all_files,
        on_button_pressed=None,
    )


def fill_device_lists(self, df):
    tables = get_device_tables(self)
    for table in tables:
        fill_specific_device_list(self, table=table, df=df)

    QtWidgets.QMessageBox.information(
        self, "Abgeschlossen!", "Geräteliste wurden geladen!"
    )


@customize_table_row
def fill_specific_device_list(self, table: QtWidgets.QTableWidget, df: pd.DataFrame):

    put_non_bl_articles_on_table(table, df, import_column_count=4)
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


def collect_data_from_table(table, article_no_col_index, discard_columns):
    """Sammle Daten aus der Tabelle."""
    data_set = set()
    for row in range(table.rowCount()):
        section_item = table.item(row, article_no_col_index)
        if section_item is not None:
            section = section_item.text()
            for column in range(5, table.columnCount()):
                column_header = table.horizontalHeaderItem(column).text()
                if column_header not in discard_columns:
                    option_item = table.horizontalHeaderItem(column)
                    value_item = table.item(row, column)
                    if option_item is not None and value_item is not None:
                        option = option_item.text()
                        value = (
                            value_item.text() if value_item.text() is not None else ""
                        )
                        data_set.add((section, option, value))
    return data_set


def check_specs_in_device_tables(self):

    device_tables = get_device_tables(self)
    fixed_val_columns = get_fixed_val_columns()

    data_set = set()
    for table in device_tables:
        # Suche den Index der 'Artikelnummer'-Spalte in einer der Tabellen

        article_no_col_index = get_column_index(table, "Artikelnummer")

        # Beende die Funktion, wenn die 'Artikelnummer'-Spalte nicht gefunden wurde
        if article_no_col_index is None:
            continue

        data_set |= collect_data_from_table(
            table, article_no_col_index, fixed_val_columns
        )

    # Sortiere das data_set nach der section
    sorted_data_set = sorted(data_set, key=lambda x: x[0])

    # Aktualisiere die Gerätespezifikationsliste
    logs_and_config.update_device_related_storage_list(
        "device_specs_list_path", sorted_data_set
    )


def fill_device_specs_in_device_tables(table):

    fixed_val_columns = get_fixed_val_columns()

    # Finde Spaltenindex der Artikelnummer
    article_no_col_index = get_column_index(table, "Artikelnummer")

    for row in range(0, table.rowCount()):
        for column in range(5, table.columnCount()):
            column_header = table.horizontalHeaderItem(column).text()
            if column_header not in fixed_val_columns:
                article_no = table.item(row, article_no_col_index).text()
                value = logs_and_config.read_device_related_storage_list(
                    "device_specs_list_path", article_no, column_header
                )
                if value is not None:
                    table.setItem(row, column, QtWidgets.QTableWidgetItem(value))


def fill_tables_content(self, saved_tables_content):
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


@customize_table_row
def fill_bl_tables(self, device_table_name: str, table: QtWidgets.QTableWidget) -> None:
    from ui.tables.utils import import_from_df_row

    bl_article_data = get_data_of_articles_from_bl(table_name=device_table_name)

    # Zum Sicherstellen dass bl_articles eine Instanz von List ist und ein Element hat
    if isinstance(bl_article_data, list) and bl_article_data:
        for data in bl_article_data:
            # Import data from each row of the blacklist articles
            import_from_df_row(table, data_row=data, import_column_count=3)


def remove_article_from_table_row(
    table: QTableWidget = None, push_button: QPushButton = None
):
    from blacklist.blacklist_gui import update_blacklist

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


def remove_articles_from_table(table):
    from blacklist.blacklist_gui import update_blacklist

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

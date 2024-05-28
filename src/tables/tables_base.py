import pandas as pd

from qtpy import QtCore, QtWidgets

from files import blacklist_base, logs_and_config

from tables.customize_row import customize_table_row
from tables import search_bar

import ui_fields.ui_fields_base
from files import blacklist_base


def connect_table_buttons(self):
    tables = ui_fields.ui_fields_base.get_device_tables(self)

    for table in tables:
        button, text_edit = search_bar.add_table_header_search_box(
            table=table, layout=self.ui.verticalLayout_3)
        search_bar.init_search_button_click_signal(table=table,
                                                   button=button,
                                                   text_edit=text_edit)
        blacklist_base.init_blacklist_button_click_signal(self, table=table)

    tables = ui_fields.ui_fields_base.get_articles_table(self)
    for table in tables:
        button, text_edit = search_bar.add_table_header_search_box(
            table=table, layout=self.ui.verticalLayout)
        search_bar.init_search_button_click_signal(table=table,
                                                   button=button,
                                                   text_edit=text_edit)


def connect_sort_indicator_changed(self):
    tables = ui_fields.ui_fields_base.get_all_tables(self)
    for table in tables:
        # Verwendung von lambda-Funktion, um das Argument "table" zu übergeben
        table.horizontalHeader().sortIndicatorChanged.connect(
            lambda sortIndex, order, table=table: on_sort_indicator_changed(self, table=table))


@customize_table_row
def on_sort_indicator_changed(self, table):
    pass


@customize_table_row
def fill_article_table(self, table, df=None):
    clear_table(table=table)

    if df is not None:
        for _, df_row in df.iterrows():
            import_from_df_row(table, data_row=df_row, import_column_count=3)

    resize_columns_to_contents(table=table)
    disable_colums_edit(table, firstcol=1, lastcol=4)


def fill_device_lists(self, df):
    tables = ui_fields.ui_fields_base.get_device_tables(self)
    for table in tables:
        fill_specific_device_list(self, table=table, df=df)

    QtWidgets.QMessageBox.information(
        self, "Abgeschlossen!", "Geräteliste wurden geladen!")


@customize_table_row
def fill_specific_device_list(self, table, df):

    table_name = table.objectName()
    # Laden Sie die Artikelnummern aus der Blacklist
    blacklist_article_numbers = [number for number, _ in blacklist_base.read_blacklist_articles(
        table_name=table_name)]
    clear_table(table)
    if df is not None:
        for _, df_row in df.iterrows():
            # Überprüfen Sie, ob die Artikelnummer nicht in der Blacklist enthalten ist
            if str(df_row.iloc[0]) not in blacklist_article_numbers:
                import_from_df_row(table, data_row=df_row,
                                   import_column_count=4)

    # Anzahl der Spalten ist flexibel, muss später angepasst hinzugefügt werden
    fill_device_specs_in_device_tables(table)
    resize_columns_to_contents(table=table)
    disable_colums_edit(table, firstcol=1, lastcol=5)


def import_from_df_row(table, data_row=None, import_column_count=None):
    tw_row = table.rowCount()
    table.insertRow(tw_row)

    # Spalte 1 (statisch) mit einer Checkbox
    checkbox_item = QtWidgets.QTableWidgetItem()
    checkbox_item.setFlags(
        QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
    checkbox_item.setCheckState(QtCore.Qt.Checked)

    # Spalte 1 mit der CheckBox
    table.setItem(tw_row, 0, checkbox_item)

    for index in range(import_column_count):
        if isinstance(data_row, pd.Series):
            item_col = QtWidgets.QTableWidgetItem(str(data_row.iloc[index]))

        elif isinstance(data_row, tuple):
            item_col = QtWidgets.QTableWidgetItem(str(data_row[index]))

        table.setItem(tw_row, index + 1, item_col)


def adding_specific_columns(self, table, tw_row=None, df_row=None):
    if table == self.ui.PV_modules_list:
        # Spalte 6 (dynamisch) mit den Werten aus der Spalte 4 des DataFrames
        table.setItem(
            tw_row, 5, QtWidgets.QTableWidgetItem(''))

    if table == self.ui.PV_inverters_list:
        # Spalte 6 (dynamisch) mit den Werten aus der Spalte 4 des DataFrames
        table.setItem(
            tw_row, 5, QtWidgets.QTableWidgetItem(''))

    if table == self.ui.BAT_inverters_list:
        # Spalte 6 (dynamisch) mit den Werten aus der Spalte 4 des DataFrames
        table.setItem(
            tw_row, 5, QtWidgets.QTableWidgetItem(''))
        # Spalte 7 (dynamisch) mit den Werten aus der Spalte 5 des DataFrames
        table.setItem(
            tw_row, 6, QtWidgets.QTableWidgetItem(''))

    if table == self.ui.BAT_storage_list:
        # Spalte 6 (dynamisch) mit den Werten aus der Spalte 4 des DataFrames
        table.setItem(
            tw_row, 5, QtWidgets.QTableWidgetItem(''))
        # Spalte 7 (dynamisch) mit den Werten aus der Spalte 5 des DataFrames
        table.setItem(
            tw_row, 6, QtWidgets.QTableWidgetItem(''))
        # Spalte 8 (dynamisch) mit den Werten aus der Spalte 6 des DataFrames
        table.setItem(
            tw_row, 7, QtWidgets.QTableWidgetItem(''))
        # Spalte 9 (dynamisch) mit den Werten aus der Spalte 7 des DataFrames
        table.setItem(
            tw_row, 8, QtWidgets.QTableWidgetItem(''))

    if table == self.ui.CHG_point_list:
        pass


def remove_articles_from_table(table):
    # Holen Sie sich alle ausgewählten Dateien im Table Widget
    df = pd.DataFrame(columns=['article_no', 'article_name'])
    rows_to_remove = []
    for row in range(table.rowCount()):
        checkbox_item = table.item(row, 0)
        article_no = table.item(row, 1).text()
        article_name = table.item(row, 2).text()

        # Überprüfe, ob die Checkbox in der aktuellen Zeile angehakt ist
        if checkbox_item and checkbox_item.checkState() == QtCore.Qt.Checked:

            new_data = pd.DataFrame(
                {'article_no': [article_no],
                 'article_name': [article_name]
                 })
            # Füge die neuen Daten zum vorhandenen DataFrame hinzu
            df = pd.concat([df, new_data], ignore_index=True)
            rows_to_remove.append(row)
    # Entfernen Sie die ausgewählten Zeilen
    for row in reversed(rows_to_remove):
        table.removeRow(row)

    blacklist_base.update_blacklist(df, table.objectName())

def clear_table(table):
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
                        value = value_item.text() if value_item.text() is not None else ""
                        data_set.add((section, option, value))
    return data_set


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


def get_fixed_val_columns():
    discard_columns = ['<>',
                       'Menge verbraucht [Stk.]',
                       'Seriennummer',
                       'Artikelnummer']
    return discard_columns


def check_specs_in_device_tables(self):

    device_tables = ui_fields.ui_fields_base.get_device_tables(self)
    fixed_val_columns = get_fixed_val_columns()

    data_set = set()
    for table in device_tables:
        # Suche den Index der 'Artikelnummer'-Spalte in einer der Tabellen

        article_no_col_index = get_column_index(
            table, 'Artikelnummer')

        # Beende die Funktion, wenn die 'Artikelnummer'-Spalte nicht gefunden wurde
        if article_no_col_index is None:
            continue

        data_set |= collect_data_from_table(
            table, article_no_col_index, fixed_val_columns)

    # Sortiere das data_set nach der section
    sorted_data_set = sorted(data_set, key=lambda x: x[0])

    # Aktualisiere die Gerätespezifikationsliste
    logs_and_config.update_device_related_storage_list(
        'device_specs_list_path', sorted_data_set)


def fill_device_specs_in_device_tables(table):

    fixed_val_columns = get_fixed_val_columns()

    # Finde Spaltenindex der Artikelnummer
    article_no_col_index = get_column_index(
        table, 'Artikelnummer')

    for row in range(0, table.rowCount()):
        for column in range(5, table.columnCount()):
            column_header = table.horizontalHeaderItem(column).text()
            if column_header not in fixed_val_columns:
                article_no = table.item(row, article_no_col_index).text()
                value = logs_and_config.read_device_related_storage_list(
                    'device_specs_list_path', article_no, column_header)
                if value is not None:
                    table.setItem(
                        row, column, QtWidgets.QTableWidgetItem(value))


def fill_tables_content(self, saved_tables_content):
    # Alle Tabellen holen
    tables = ui_fields.ui_fields_base.get_all_tables(self)
    for table in tables:
        clear_table(table)

    # Durch jedes Element im gespeicherten Tabelleninhalt iterieren
    for table_map, value in saved_tables_content.items():
        # Tabellennamen, Zeile und Spalte extrahieren
        table_name = table_map.split('(')[0]
        table_row = int(table_map.split('(')[1].split(';')[0])
        table_column = int(table_map.split('(')[1].split(';')[1].split(')')[0])

        # Durch jede Qt-Tabelle iterieren
        for table in tables:

            # Wenn der Tabellenname übereinstimmt
            if table_name == table.objectName().lower():
                # Wenn die Anzahl der Zeilen kleiner oder gleich der Zielzeile ist
                if table.rowCount() <= table_row:
                    # Differenz berechnen und fehlende Zeilen einfügen
                    diff = table_row - table.rowCount()
                    for _ in range(diff + 1):
                        table.insertRow(table.rowCount())

                # Checkbox in Spalte 1 setzen
                checkbox_item = QtWidgets.QTableWidgetItem()
                checkbox_item.setFlags(
                    QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                checkbox_item.setCheckState(QtCore.Qt.Checked)

                # Checkbox in die Tabelle einfügen
                table.setItem(table_row, 0, checkbox_item)

                # Wert in die spezifische Spalte einfügen
                # Hier wird der Wert in ein QTableWidgetItem-Objekt konvertiert
                value_item = QtWidgets.QTableWidgetItem(str(value))
                table.setItem(table_row, table_column, value_item)

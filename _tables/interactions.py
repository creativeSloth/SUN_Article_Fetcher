import pandas as pd

from qtpy import QtCore, QtWidgets, QtGui

from odf.opendocument import load

import logs_and_config

from _tables.row_colour import change_table_row_colour
import _ui_fields_Handler.ui_fields


def connect_sort_indicator_changed(self):
    tables = _ui_fields_Handler.ui_fields.get_all_tables(self)
    for table in tables:
        # Verwendung von lambda-Funktion, um das Argument "table" zu übergeben
        table.horizontalHeader().sortIndicatorChanged.connect(
            lambda sortIndex, order, table=table: on_sort_indicator_changed(self, table=table))


@change_table_row_colour
def on_sort_indicator_changed(self, table):
    pass


def change_foreground_if_zero(count, table, row):
    if count == 0:
        for column in range(1, table.columnCount()):
            table.item(row, column).setForeground(
                QtGui.QColor("#e20000"))


@change_table_row_colour
def fill_article_table(self, table, df=None):
    clear_table(table=table)

    if df is not None:
        for _, df_row in df.iterrows():

            tw_row = table.rowCount()
            table.insertRow(tw_row)

            # Spalte 1 (statisch) mit einer Checkbox
            checkbox_item = QtWidgets.QTableWidgetItem()
            checkbox_item.setFlags(
                QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            checkbox_item.setCheckState(QtCore.Qt.Checked)

            # Spalte 1 mit der CheckBox
            table.setItem(tw_row, 0, checkbox_item)

            # Spalte 2 (dynamisch) mit den Werten aus der Spalte 0 des DataFrames
            item_col1 = QtWidgets.QTableWidgetItem(str(df_row.iloc[0]))
            table.setItem(tw_row, 1, item_col1)

            # Spalte 3 (dynamisch) mit den Werten aus der Spalte 1 des DataFrames
            item_col2 = QtWidgets.QTableWidgetItem(str(df_row.iloc[1]))
            table.setItem(tw_row, 2, item_col2)
            # Spalte 4 (dynamisch) mit den Werten aus der Spalte 2 des DataFrames
            if df_row.shape[0] >= 3:  # !!!!!!!!
                item_col3 = QtWidgets.QTableWidgetItem(str(df_row.iloc[2]))
                table.setItem(tw_row, 3, item_col3)
            change_foreground_if_zero(df_row.iloc[2], table, tw_row)

    # Iteriere über alle Zellen im Table Widget
    for row in range(table.rowCount()):
        for col in range(table.columnCount()):
            item = table.item(row, col)
            if item:
                # Deaktiviere die Editierbarkeit für die Zelle
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

    resize_columns_to_contents(list=table, columns=table.columnCount())


def fill_device_lists(self, df):
    tables = _ui_fields_Handler.ui_fields.get_device_tables(self)
    for table in tables:
        fill_specific_device_list(self, table=table, df=df)

    QtWidgets.QMessageBox.information(
        self, "Abgeschlossen!", "Geräteliste wurden geladen!")


@change_table_row_colour
def fill_specific_device_list(self, table, df):

    clear_table(table)

    # Laden Sie die Artikelnummern aus der Blacklist
    blacklist_article_numbers = logs_and_config.read_blacklist_article_numbers(
        self, table_name=table.objectName())

    if df is not None:
        for _, df_row in df.iterrows():
            # Überprüfen Sie, ob die Artikelnummer nicht in der Blacklist enthalten ist
            if str(df_row.iloc[0]) not in blacklist_article_numbers:
                tw_row = table.rowCount()
                table.insertRow(tw_row)

                # Spalte 1 (statisch) mit einer Checkbox
                checkbox_item = QtWidgets.QTableWidgetItem()
                checkbox_item.setFlags(
                    QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                checkbox_item.setCheckState(QtCore.Qt.Checked)

                # Spalte 1 mit der CheckBox
                table.setItem(tw_row, 0, checkbox_item)

                # Spalte 2 (dynamisch) mit den Werten aus der Spalte 0 des DataFrames
                table.setItem(
                    tw_row, 1, QtWidgets.QTableWidgetItem(str(df_row.iloc[0])))

                # Spalte 3 (dynamisch) mit den Werten aus der Spalte 1 des DataFrames
                table.setItem(
                    tw_row, 2, QtWidgets.QTableWidgetItem(str(df_row.iloc[1])))

                # Spalte 4 (dynamisch) mit den Werten aus der Spalte 2 des DataFrames
                table.setItem(
                    tw_row, 3, QtWidgets.QTableWidgetItem(str(df_row.iloc[2])))

                # Spalte 5 (dynamisch) mit den Werten aus der Spalte 3 des DataFrames
                table.setItem(
                    tw_row, 4, QtWidgets.QTableWidgetItem(str(df_row.iloc[3])))
                ui_list_to_df_mapping(self, table, tw_row, df_row)
                change_foreground_if_zero(df_row.iloc[2], table, tw_row)
    # Anzahl der Spalten ist flexibel, muss später angepasst hinzugefügt werden
    fill_device_specs_in_device_tables(self, table)
    resize_columns_to_contents(list=table, columns=table.columnCount())
    disable_colums_edit(table, firstcol=1, lastcol=5)


def ui_list_to_df_mapping(self, ui_list, tw_row=None, df_row=None):
    if ui_list == self.ui.PV_modules_list:
        # Spalte 6 (dynamisch) mit den Werten aus der Spalte 4 des DataFrames
        ui_list.setItem(
            tw_row, 5, QtWidgets.QTableWidgetItem(''))

    if ui_list == self.ui.PV_inverters_list:
        # Spalte 6 (dynamisch) mit den Werten aus der Spalte 4 des DataFrames
        ui_list.setItem(
            tw_row, 5, QtWidgets.QTableWidgetItem(''))

    if ui_list == self.ui.BAT_inverters_list:
        # Spalte 6 (dynamisch) mit den Werten aus der Spalte 4 des DataFrames
        ui_list.setItem(
            tw_row, 5, QtWidgets.QTableWidgetItem(''))
        # Spalte 7 (dynamisch) mit den Werten aus der Spalte 5 des DataFrames
        ui_list.setItem(
            tw_row, 6, QtWidgets.QTableWidgetItem(''))

    if ui_list == self.ui.BAT_storage_list:
        # Spalte 6 (dynamisch) mit den Werten aus der Spalte 4 des DataFrames
        ui_list.setItem(
            tw_row, 5, QtWidgets.QTableWidgetItem(''))
        # Spalte 7 (dynamisch) mit den Werten aus der Spalte 5 des DataFrames
        ui_list.setItem(
            tw_row, 6, QtWidgets.QTableWidgetItem(''))
        # Spalte 8 (dynamisch) mit den Werten aus der Spalte 6 des DataFrames
        ui_list.setItem(
            tw_row, 7, QtWidgets.QTableWidgetItem(''))
        # Spalte 9 (dynamisch) mit den Werten aus der Spalte 7 des DataFrames
        ui_list.setItem(
            tw_row, 8, QtWidgets.QTableWidgetItem(''))

    if ui_list == self.ui.CHG_point_list:
        pass


def remove_articles_from_list(self, list):
    # Holen Sie sich alle ausgewählten Dateien im Table Widget
    df = pd.DataFrame(columns=['article_no', 'article_name'])
    rows_to_remove = []
    for row in range(list.rowCount()):
        checkbox_item = list.item(row, 0)
        article_no = list.item(row, 1).text()
        article_name = list.item(row, 2).text()

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
        list.removeRow(row)

    logs_and_config.update_blacklist(self, df, list.objectName())


def clear_table(table):
    # Setze die Anzahl der Zeilen auf 0, um alle Zeilen zu entfernen
    table.setRowCount(0)


def resize_columns_to_contents(list, columns):
    header = list.horizontalHeader()
    for i in range(columns):
        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)


def get_column_index(list, column):
    """Suche den Index der 'Artikelnummer'-Spalte in der Tabelle."""
    column_index = None
    for column_index in range(list.columnCount()):
        if list.horizontalHeaderItem(column_index).text() == column:
            return column_index
    return None


def collect_data_from_table(table, article_no_col_index, discard_columns):
    """Sammle Daten aus der Tabelle."""
    data_set = set()
    for row in range(table.rowCount()):
        section_item = table.item(row, article_no_col_index)
        if section_item is not None:
            section = section_item.text()
            for column in range(table.columnCount()):
                column_header = table.horizontalHeaderItem(column).text()
                if column_header not in discard_columns:
                    option_item = table.horizontalHeaderItem(column)
                    value_item = table.item(row, column)
                    if option_item is not None and value_item is not None:
                        option = option_item.text()
                        value = value_item.text() if value_item.text() is not None else ""
                        data_set.add((section, option, value))
    return data_set


def disable_colums_edit(ui_list, firstcol, lastcol):
    for row in range(ui_list.rowCount()):
        for col in range(firstcol, lastcol):
            # Das vorhandene QTableWidgetItem abrufen
            item = ui_list.item(row, col)
            # Entfernt das Bearbeitungsflag für die 2. Spaltess
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)


def get_fixed_val_columns():
    discard_columns = ['<>',
                       'Anzahl [Stk.]',
                       'Seriennummer',
                       'Artikelnummer']
    return discard_columns


def check_specs_in_device_tables(self):

    device_tables = _ui_fields_Handler.ui_fields.get_device_tables(self)
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
        self, 'device_specs_list_path', sorted_data_set
    )


def fill_device_specs_in_device_tables(self, ui_list):

    fixed_val_columns = get_fixed_val_columns()

    # Finde Spaltenindex der Artikelnummer
    article_no_col_index = get_column_index(
        ui_list, 'Artikelnummer')

    for row in range(0, ui_list.rowCount()):
        for column in range(5, ui_list.columnCount()):
            column_header = ui_list.horizontalHeaderItem(column).text()
            if column_header not in fixed_val_columns:
                article_no = ui_list.item(row, article_no_col_index).text()
                value = logs_and_config.read_device_related_storage_list(
                    self, 'device_specs_list_path', article_no, column_header)
                if value is not None:
                    ui_list.setItem(
                        row, column, QtWidgets.QTableWidgetItem(value))


def fill_tables_content(self, saved_tables_content):
    # Alle Tabellen holen
    tables = _ui_fields_Handler.ui_fields.get_all_tables(self)
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

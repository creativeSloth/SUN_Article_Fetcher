import os
from qtpy import QtCore, QtWidgets

import pandas as pd

from odf.opendocument import load
from odf import text, teletype
from odf.table import Table, TableRow, TableCell

import logs_and_config
import directory_Handler
import data_Handler


def config_to_fields(self):
    try:
        self.ui.db_server.setPlainText(
            logs_and_config.read_config_value(self, 'Server', 'server'))
        self.ui.user.setPlainText(
            logs_and_config.read_config_value(self, 'Server', 'user'))
        self.ui.pw.setPlainText(
            logs_and_config.read_config_value(self, 'Server', 'password'))
        self.ui.db_name.setPlainText(
            logs_and_config.read_config_value(self, 'Server', 'dB_name'))
        self.ui.query_input.setPlainText(
            logs_and_config.read_config_value(self, 'Abfrage', 'sql1'))
        self.ui.query_2_input.setPlainText(
            logs_and_config.read_config_value(self, 'Abfrage', 'sql2'))
        self.ui.source_path_text.setPlainText(
            logs_and_config.read_config_value(self, 'Pfade', 'source_path'))
        self.ui.target_path_text.setPlainText(
            logs_and_config.read_config_value(self, 'Pfade', 'target_path'))
        self.ui.target_path_text_2.setPlainText(
            logs_and_config.read_config_value(self, 'Pfade', 'target_path_2'))
        self.ui.source_path_text_matstr.setPlainText(
            logs_and_config.read_config_value(self, 'Pfade', 'template1_path'))
        self.ui.source_path_text_docu.setPlainText(
            logs_and_config.read_config_value(self, 'Pfade', 'template2_path'))
    except Exception as e:
        QtWidgets.QMessageBox.warning(
            self, "Fehler", f"Konfigurationsdaten konnten nicht geladen werden, daher wurde eine neue Konfigurationsdatei erstellt.\n\n"
            f"Fehlermeldung:\n {e}")
        config_path = directory_Handler.get_directories(self)['config_path']
        if os.path.exists(config_path):
            os.remove(config_path)
        logs_and_config.create_config_file(self)


def char_validation(self):
    textlength = 10
    # Speichere den vorherigen Text
    prev_string = self.previous_project_text
    current_string = self.project
    cursor = self.ui.project.textCursor()
    cur_cursor_pos = cursor.position()

    # Überprüfe, ob die Länge des aktuellen Strings größer als 10 ist
    if len(current_string) > textlength:
        # Aktuellen Text durch den vorherigen Text ersetzen
        current_string = prev_string
        # Speichere die Position des Cursors vor der Änderung
        prev_cursor_pos = cur_cursor_pos - 1
        # Setze den Text des Textfeldes auf den aktuellen Text
        self.ui.project.setPlainText(current_string)
        # Setze den Cursor wieder auf seine vorherige Position
        cur_cursor_pos = prev_cursor_pos

    # Setze den Cursor auf die vorherige Position
    cursor.setPosition(cur_cursor_pos)

    # Wandle den Text in Großbuchstaben um und aktualisiere den Text im Textfeld
    uppercase_string = project_to_uppercase(self,
                                            current_string, cur_cursor_pos)

    # Aktualisiere den Textcursor im Textfeld
    self.ui.project.setTextCursor(cursor)

    # Speichere den aktuellen Text als den vorherigen Text
    self.previous_project_text = uppercase_string


def project_to_uppercase(self, text, cur_cursor_pos):
    if any(char.islower() for char in text):
        # Wandle den Text in Großbuchstaben um
        uppercase_string = "".join(
            char.upper() if char.islower() else char for char in text)
        # Setze den Text des Textfeldes auf den umgewandelten Text
        self.ui.project.setPlainText(uppercase_string)
        cursor = self.ui.project.textCursor()
        cursor.setPosition(cur_cursor_pos)
        return uppercase_string
    else:
        return text


def get_mapped_context(self):
    return {
        '{{project}}': (self.ui.project, ''),
        '{{operator}}': (self.ui.operator_text, 'data_2'),
        '{{op_adress_1}}': (self.ui.op_adress_1_text, 'data_3'),
        '{{op_adress_2}}': (self.ui.op_adress_2_text, 'data_4'),
        '{{op_adress_3}}': (self.ui.op_adress_3_text, 'data_5'),
        '{{loc_adress_1}}': (self.ui.loc_adress_1_text, 'data_6'),
        '{{loc_adress_2}}': (self.ui.loc_adress_2_text, 'data_7'),
        '{{loc_adress_3}}': (self.ui.loc_adress_3_text, 'data_8'),
        '{{sys_perf}}': (self.ui.sys_perf_text, 'data_9'),
        '{{constr_style}}': (self.ui.constr_style_text, 'data_10'),
        '{{bool_consist_azimuth}}': (self.ui.bool_consist_azimuth_text, 'data_11'),
        '{{maj_azimuth}}': (self.ui.maj_azimuth_text, 'data_12'),
        '{{maj_card_point}}': (self.ui.maj_card_point_text, 'data_13'),
        '{{min_azimuth}}': (self.ui.min_azimuth_text, 'data_14'),
        '{{min_card_point}}': (self.ui.min_card_point_text, 'data_15'),
        '{{maj_tilt}}': (self.ui.maj_tilt_text, 'data_16'),
        '{{min_tilt}}': (self.ui.min_tilt_text, 'data_17'),
        '{{module_count}}': (self.ui.module_count_text, 'data_18'),
        '{{module_type}}': (self.ui.module_type_text, data_Handler.aggr_dev_list(self.ui.PV_modules_list, 2)),
        '{{mounting_type}}': (self.ui.mounting_type_text, 'data_20'),
        '{{hybrid_inverter_bool}}': (self.ui.hybrid_inverter_bool_text, 'data_21'),
        '{{inverter_type}}': (self.ui.inverter_type_text, data_Handler.aggr_dev_list(self.ui.PV_inverters_list, 2)),
        '{{inverter_SN}}': (self.ui.inverter_SN_text, data_Handler.aggr_dev_list(self.ui.PV_inverters_list, 4)),
        '{{inverter_power}}': (self.ui.inverter_power_text, data_Handler.aggr_dev_list(self.ui.PV_inverters_list, 5)),
        '{{commiss_date}}': (self.ui.commiss_date_text, 'data_25'),
        '{{bat_inverter_type}}': (self.ui.bat_inverter_type_text, data_Handler.aggr_dev_list(self.ui.BAT_inverters_list, 2)),
        '{{bat_inverter_SN}}': (self.ui.bat_inverter_SN_text, data_Handler.aggr_dev_list(self.ui.BAT_inverters_list, 4)),
        '{{bat_inverter_power}}': (self.ui.bat_inverter_power_text, data_Handler.aggr_dev_list(self.ui.BAT_inverters_list, 5)),
        '{{coupling_type}}': (self.ui.coupling_type_text, data_Handler.aggr_dev_list(self.ui.BAT_inverters_list, 6)),
        '{{bat_storage_type}}': (self.ui.bat_storage_type_text, data_Handler.aggr_dev_list(self.ui.BAT_storage_list, 2)),
        '{{bat_storage_SN}}': (self.ui.bat_storage_SN_text, data_Handler.aggr_dev_list(self.ui.BAT_storage_list, 4)),
        '{{bat_storage_cap}}': (self.ui.bat_storage_cap_text, data_Handler.aggr_dev_list(self.ui.BAT_storage_list, 5)),
        '{{bat_commiss_date}}': (self.ui.bat_commiss_date_text, 'data_33'),
        '{{max_discharge_pow}}': (self.ui.max_discharge_pow_text, data_Handler.aggr_dev_list(self.ui.BAT_storage_list, 6)),
        '{{em_pow_ability_bool}}': (self.ui.em_pow_ability_bool_text, 'data_35'),
        '{{energy_storage_type}}': (self.ui.energy_storage_type_text, 'data_36'),
        '{{bat_technology}}': (self.ui.bat_technology_text, 'data_37'),
        '{{charging_point_type}}': (self.ui.charging_point_type_text, data_Handler.aggr_dev_list(self.ui.CHG_point_list, 2)),
        '{{charging_point_SN}}': (self.ui.charging_point_SN_text, data_Handler.aggr_dev_list(self.ui.CHG_point_list, 4)),
        '{{feeding_type}}': (self.ui.feeding_type_text, 'data_40'),
        '{{pow_limit_bool}}': (self.ui.pow_limit_bool_text, 'data_41'),
        '{{rmt_grd_op_bool}}': (self.ui.rmt_grd_op_bool_text, 'data_42'),
        '{{rmt_drct_mrktr_bool}}': (self.ui.rmt_drct_mrktr_bool_text, 'data_43'),
        '{{rmt_3rd_prt_bool}}': (self.ui.rmt_3rd_prt_bool_text, 'data_44'),
        '{{prequali_bool}}': (self.ui.prequali_bool_text, 'data_45'),
        '{{citizen_corp_bool}}': (self.ui.citizen_corp_bool_text, 'data_46'),
        '{{tendering_bool}}': (self.ui.tendering_bool_text, 'data_47'),
        '{{meter_cabinet}}': (self.ui.meter_cabinet_text, 'data_48'),
        '{{meter_box_type}}': (self.ui.meter_box_type_text, 'data_49'),
        '{{dl_type}}': (self.ui.dl_type_text, 'data_50'),
        '{{dl_connect_ext}}': (self.ui.dl_connect_ext_text, 'data_51')
    }


def fill_docu_fields(self):
    [value[0].setPlainText(value[1])
     for value in get_mapped_context(self).values()
     if value[0] != self.ui.project]


def clear_docu_fields(self):
    [value[0].clear()
     for value in get_mapped_context(self).values()
     if value[0] != self.ui.project]


def fill_article_list(self, df=None):
    ui_list = self.ui.articles_list
    clear_article_list(self, list=ui_list)
    if df is not None:
        for _, df_row in df.iterrows():

            tw_row = ui_list.rowCount()
            ui_list.insertRow(tw_row)

            # Spalte 1 (statisch) mit einer Checkbox
            checkbox_item = QtWidgets.QTableWidgetItem()
            checkbox_item.setFlags(
                QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            checkbox_item.setCheckState(QtCore.Qt.Checked)

            # Spalte 1 mit der CheckBox
            ui_list.setItem(tw_row, 0, checkbox_item)

            # Spalte 2 (dynamisch) mit den Werten aus der Spalte 0 des DataFrames
            item_col1 = QtWidgets.QTableWidgetItem(str(df_row.iloc[0]))
            ui_list.setItem(tw_row, 1, item_col1)
            # Spalte 3 (dynamisch) mit den Werten aus der Spalte 1 des DataFrames
            item_col2 = QtWidgets.QTableWidgetItem(str(df_row.iloc[1]))
            ui_list.setItem(tw_row, 2, item_col2)
            # Spalte 4 (dynamisch) mit den Werten aus der Spalte 2 des DataFrames
            if df_row.shape[0] >= 3:  # !!!!!!!!
                item_col3 = QtWidgets.QTableWidgetItem(str(df_row.iloc[2]))
                ui_list.setItem(tw_row, 3, item_col3)

    # Iteriere über alle Zellen im Table Widget
    for row in range(ui_list.rowCount()):
        for col in range(ui_list.columnCount()):
            item = ui_list.item(row, col)
            if item:
                # Deaktiviere die Editierbarkeit für die Zelle
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

    resize_columns_to_contents(
        self, list=ui_list, columns=ui_list.columnCount())


@directory_Handler.check_path_existence(modus=1)
def replace_fields_in_doc1(self):
    # Rufe get_directories auf, um die Pfade zu erhalten
    template1_path = directory_Handler.get_directories(self)[
        'template1_path']
    doc1_path = directory_Handler.get_directories(self)[
        'doc1_path']

    try:
        doc1 = load(template1_path)
        context = get_mapped_context(self)

        # Durchlaufe alle Tabellen in der ODF-Datei
        for table in doc1.getElementsByType(Table):
            # Durchlaufe alle Zeilen in der Tabelle
            for row in table.getElementsByType(TableRow):
                # Durchlaufe alle Zellen in der Zeile
                for cell in row.getElementsByType(TableCell):
                    # Text in der Zelle erhalten
                    cell_text = ""
                    Flag = False
                    for text_node in cell.getElementsByType(text.P):
                        cell_text = teletype.extractText(text_node)
                        cell_format = text_node.getAttribute(
                            "stylename")

                        for field_name, field_val in context.items():
                            field_values = field_val[0].toPlainText().split(
                                '\n')

                            if field_name in cell_text:
                                Flag = True

                                for field_value in field_values:
                                    # Erstelle einen neuen Textknoten mit dem aktualisierten Text und Format
                                    new_text_node = text.P(
                                        text=str(field_value))
                                    new_text_node.setAttribute(
                                        ("stylename"), cell_format)

                                    # Füge den neuen Textknoten in die Zelle ein
                                    cell.addElement(new_text_node)
                                    # Entferne den alten Textknoten
                        if Flag == True:
                            cell.removeChild(text_node)
                            Flag = False

        doc1.save(doc1_path)
        QtWidgets.QMessageBox.information(
            self, "Abgeschlossen!",
            f"Die Datei wurde unter folgendem Pfad gespeichert:\n"
            f"{doc1_path}")

    except Exception as e:
        QtWidgets.QMessageBox.warning(
            self, "Fehler", f"Fehler bei der Feldersetzung: {e}")


def fill_device_lists(self, df):
    tables = get_device_tables(self)
    for table in tables:

        fill_specific_device_list(self, df, ui_list=table)

    QtWidgets.QMessageBox.information(
        self, "Abgeschlossen!", "Geräteliste wurden geladen!")


def fill_specific_device_list(self, df=None, ui_list=None):

    clear_article_list(self, list=ui_list)

    # Laden Sie die Artikelnummern aus der Blacklist
    blacklist_article_numbers = logs_and_config.read_blacklist_article_numbers(
        self, list_name=ui_list.objectName())

    if df is not None:
        for _, df_row in df.iterrows():
            # Überprüfen Sie, ob die Artikelnummer nicht in der Blacklist enthalten ist
            if str(df_row.iloc[0]) not in blacklist_article_numbers:
                tw_row = ui_list.rowCount()
                ui_list.insertRow(tw_row)

                # Spalte 1 (statisch) mit einer Checkbox
                checkbox_item = QtWidgets.QTableWidgetItem()
                checkbox_item.setFlags(
                    QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                checkbox_item.setCheckState(QtCore.Qt.Checked)

                # Spalte 1 mit der CheckBox
                ui_list.setItem(tw_row, 0, checkbox_item)

                # Spalte 2 (dynamisch) mit den Werten aus der Spalte 0 des DataFrames
                ui_list.setItem(
                    tw_row, 1, QtWidgets.QTableWidgetItem(str(df_row.iloc[0])))

                # Spalte 3 (dynamisch) mit den Werten aus der Spalte 1 des DataFrames
                ui_list.setItem(
                    tw_row, 2, QtWidgets.QTableWidgetItem(str(df_row.iloc[1])))

                # Spalte 4 (dynamisch) mit den Werten aus der Spalte 2 des DataFrames
                ui_list.setItem(
                    tw_row, 3, QtWidgets.QTableWidgetItem(str(df_row.iloc[2])))

                # Spalte 5 (dynamisch) mit den Werten aus der Spalte 3 des DataFrames
                ui_list.setItem(
                    tw_row, 4, QtWidgets.QTableWidgetItem(str(df_row.iloc[3])))
                ui_list_to_df_mapping(self, ui_list, tw_row, df_row)
    # Anzahl der Spalten ist flexibel, muss später angepasst hinzugefügt werden
    fill_device_specs_in_device_tables(self, ui_list)
    resize_columns_to_contents(
        self, list=ui_list, columns=ui_list.columnCount())
    disable_colums_edit(ui_list, firstcol=1, lastcol=5)


def disable_colums_edit(ui_list, firstcol, lastcol):
    for row in range(ui_list.rowCount()):
        for col in range(firstcol, lastcol):
            # Das vorhandene QTableWidgetItem abrufen
            item = ui_list.item(row, col)
            # Entfernt das Bearbeitungsflag für die 2. Spaltess
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)


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
            tw_row, 7, QtWidgets.QTableWidgetItem(''))
        # Spalte 8 (dynamisch) mit den Werten aus der Spalte 6 des DataFrames
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


def clear_article_list(self, list):
    # Setze die Anzahl der Zeilen auf 0, um alle Zeilen zu entfernen
    list.setRowCount(0)


def resize_columns_to_contents(self, list, columns):
    header = list.horizontalHeader()
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


def get_device_tables(self):
    # Alle Tabellen mit PV-Geräten
    device_tables = [
        self.ui.PV_modules_list,
        self.ui.PV_inverters_list,
        self.ui.BAT_inverters_list,
        self.ui.BAT_storage_list,
        self.ui.CHG_point_list
    ]
    return device_tables


def get_articles_table(self):
    # Alle Tabellen mit PV-Geräten
    articles_table = [
        self.ui.articles_list
    ]
    return articles_table


def get_all_tables(self):
    device_tables = get_device_tables(self)
    articles_table = get_articles_table(self)
    all_tables = device_tables + articles_table

    return all_tables


def get_fixed_val_columns():
    discard_columns = ['<>',
                       'Anzahl [Stk.]',
                       'Seriennummer',
                       'Artikelnummer']
    return discard_columns


def check_specs_in_device_tables(self):

    device_tables = get_device_tables(self)
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
        for column in range(ui_list.columnCount()):
            column_header = ui_list.horizontalHeaderItem(column).text()
            if column_header not in fixed_val_columns:
                article_no = ui_list.item(row, article_no_col_index).text()
                value = logs_and_config.read_device_related_storage_list(
                    self, 'device_specs_list_path', article_no, column_header)
                if value is not None:
                    ui_list.setItem(
                        row, column, QtWidgets.QTableWidgetItem(value))


def save_fields_text(self):
    mapped_values = get_mapped_context(self).values()
    field_map = [(field[0], field[0].toPlainText()) for field in mapped_values]

    logs_and_config.create_save_file(self, field_map=field_map)


def load_fields_text(self):
    pass

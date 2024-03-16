import os
from qtpy import QtWidgets
from qtpy import QtCore
import pandas as pd

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


def get_project(self):
    return self.ui.project.toPlainText()


def char_validation(self):
    textlength = 10
    # Speichere den vorherigen Text
    prev_string = self.previous_project_text
    current_string = get_project(self)
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
        '{{project}}': (self.ui.project, 'data_1', 'default'),
        '{{operator}}': (self.ui.operator_text, 'data_2', 'default'),
        '{{op_adress_1}}': (self.ui.op_adress_1_text, 'data_3', 'default'),
        '{{op_adress_2}}': (self.ui.op_adress_2_text, 'data_4', 'default'),
        '{{op_adress_3}}': (self.ui.op_adress_3_text, 'data_5', 'default'),
        '{{loc_adress_1}}': (self.ui.loc_adress_1_text, 'data_6', 'default'),
        '{{loc_adress_2}}': (self.ui.loc_adress_2_text, 'data_7', 'default'),
        '{{loc_adress_3}}': (self.ui.loc_adress_3_text, 'data_8', 'default'),
        '{{sys_perf}}': (self.ui.sys_perf_text, 'data_9', 'default'),
        '{{constr_style}}': (self.ui.constr_style_text, 'data_10', 'default'),
        '{{bool_consist_azimuth}}': (self.ui.bool_consist_azimuth_text, 'data_11', 'default'),
        '{{maj_azimuth}}': (self.ui.maj_azimuth_text, 'data_12', 'default'),
        '{{maj_card_point}}': (self.ui.maj_card_point_text, 'data_13', 'default'),
        '{{min_azimuth}}': (self.ui.min_azimuth_text, 'data_14', 'default'),
        '{{min_card_point}}': (self.ui.min_card_point_text, 'data_15', 'default'),
        '{{maj_tilt}}': (self.ui.maj_tilt_text, 'data_16', 'default'),
        '{{min_tilt}}': (self.ui.min_tilt_text, 'data_17', 'default'),
        '{{module_count}}': (self.ui.module_count_text, 'data_18', 'default'),
        '{{module_type}}': (self.ui.module_type_text, 'data_19', 'default'),
        '{{mounting_type}}': (self.ui.mounting_type_text, 'data_20', 'default'),
        '{{hybrid_inverter_bool}}': (self.ui.hybrid_inverter_bool_text, 'data_21', 'default'),
        '{{inverter_type}}': (self.ui.inverter_type_text, data_Handler.get_inv_types(self), 'default'),
        '{{inverter_SN}}': (self.ui.inverter_SN_text, data_Handler.get_serial_of_inv(self), 'default'),
        '{{inverter_power}}': (self.ui.inverter_power_text, data_Handler.get_power_of_inv(self), 'default'),
        '{{commiss_date}}': (self.ui.commiss_date_text, 'data_25', 'default'),
        '{{bat_inverter_type}}': (self.ui.bat_inverter_type_text, 'data_26', 'default'),
        '{{bat_inverter_SN}}': (self.ui.bat_inverter_SN_text, 'data_27', 'default'),
        '{{bat_inverter_power}}': (self.ui.bat_inverter_power_text, 'data_28', 'default'),
        '{{coupling_type}}': (self.ui.coupling_type_text, 'data_29', 'default'),
        '{{bat_storage_type}}': (self.ui.bat_storage_type_text, 'data_30', 'default'),
        '{{bat_storage_SN}}': (self.ui.bat_storage_SN_text, 'data_31', 'default'),
        '{{bat_storage_cap}}': (self.ui.bat_storage_cap_text, 'data_32', 'default'),
        '{{bat_commiss_date}}': (self.ui.bat_commiss_date_text, 'data_33', 'default'),
        '{{max_discharge_pow}}': (self.ui.max_discharge_pow_text, 'data_34', 'default'),
        '{{em_pow_ability_bool}}': (self.ui.em_pow_ability_bool_text, 'data_35', 'default'),
        '{{energy_storage_type}}': (self.ui.energy_storage_type_text, 'data_36', 'default'),
        '{{bat_technology}}': (self.ui.bat_technology_text, 'data_37', 'default'),
        '{{charging_point_type}}': (self.ui.charging_point_type_text, 'data_38', 'default'),
        '{{charging_point_SN}}': (self.ui.charging_point_SN_text, 'data_39', 'default'),
        '{{feeding_type}}': (self.ui.feeding_type_text, 'data_40', 'default'),
        '{{pow_limit_bool}}': (self.ui.pow_limit_bool_text, 'data_41', 'default'),
        '{{rmt_grd_op_bool}}': (self.ui.rmt_grd_op_bool_text, 'data_42', 'default'),
        '{{rmt_drct_mrktr_bool}}': (self.ui.rmt_drct_mrktr_bool_text, 'data_43', 'default'),
        '{{rmt_3rd_prt_bool}}': (self.ui.rmt_3rd_prt_bool_text, 'data_44', 'default'),
        '{{prequali_bool}}': (self.ui.prequali_bool_text, 'data_45', 'default'),
        '{{citizen_corp_bool}}': (self.ui.citizen_corp_bool_text, 'data_46', 'default'),
        '{{tendering_bool}}': (self.ui.tendering_bool_text, 'data_47', 'default'),
        '{{meter_cabinet}}': (self.ui.meter_cabinet_text, 'data_48', 'default'),
        '{{meter_box_type}}': (self.ui.meter_box_type_text, 'data_49', 'default'),
        '{{dl_type}}': (self.ui.dl_type_text, 'data_50', 'default'),
        '{{dl_connect_ext}}': (self.ui.dl_connect_ext_text, 'data_51', 'default')
    }


def fill_docu_fields(self, df):
    [value[0].setPlainText(value[1])
     for value in get_mapped_context(self).values()
     if value[0] != self.ui.project]


def fill_device_lists(self, df):
    fill_PV_inverter_list(self, df)


def clear_docu_fields(self):
    [value[0].clear()
     for value in get_mapped_context(self).values()
     if value[0] != self.ui.project]


def fill_article_list(self, df=None):
    ui_list = self.ui.articles_list
    clear_article_list(self, list=ui_list)
    if df is not None:
        for _, row in df.iterrows():

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
            item_col1 = QtWidgets.QTableWidgetItem(str(row.iloc[0]))
            ui_list.setItem(tw_row, 1, item_col1)
            # Spalte 3 (dynamisch) mit den Werten aus der Spalte 1 des DataFrames
            item_col2 = QtWidgets.QTableWidgetItem(str(row.iloc[1]))
            ui_list.setItem(tw_row, 2, item_col2)
            #! Spalte 4 (dynamisch) mit den Werten aus der Spalte 2 des DataFrames
            if row.shape[0] == 3:
                item_col3 = QtWidgets.QTableWidgetItem(str(row.iloc[2]))
                ui_list.setItem(tw_row, 3, item_col3)

    # Iteriere über alle Zellen im Table Widget
    for row in range(ui_list.rowCount()):
        for col in range(1, ui_list.columnCount()):
            item = ui_list.item(row, col)
            if item:
                # Deaktiviere die Editierbarkeit für die Zelle
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

    resize_columns_to_contents(
        self, list=ui_list, columns=ui_list.columnCount())


def fill_PV_inverter_list(self, df=None):
    ui_list = self.ui.PV_inverters_list
    clear_article_list(self, list=ui_list)
    if df is not None:
        #!------------------------------------------------
        print('Dataframe: ' + str(df))
        for _, row in df.iterrows():
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
                tw_row, 1, QtWidgets.QTableWidgetItem(str(row.iloc[0])))

            # Spalte 3 (dynamisch) mit den Werten aus der Spalte 1 des DataFrames
            ui_list.setItem(
                tw_row, 2, QtWidgets.QTableWidgetItem(str(row.iloc[1])))

            # Spalte 4 (dynamisch) mit den Werten aus der Spalte 2 des DataFrames
            ui_list.setItem(
                tw_row, 3, QtWidgets.QTableWidgetItem(str(row.iloc[2])))

            # Spalte 5 (dynamisch) mit den Werten aus der Spalte 3 des DataFrames
            ui_list.setItem(
                tw_row, 4, QtWidgets.QTableWidgetItem(str(row.iloc[3])))

            # Spalte 6 (dynamisch) mit den Werten aus der Spalte 4 des DataFrames
            ui_list.setItem(
                tw_row, 5, QtWidgets.QTableWidgetItem('noch keine Informationsverknüpfung vorhanden'))

    # Anzahl der Spalten ist flexibel, muss später angepasst hinzugefügt werden
    resize_columns_to_contents(
        self, list=ui_list, columns=ui_list.columnCount())

    QtWidgets.QMessageBox.information(
        self, "Abgeschlossen!", "PV-Inverter Liste geladen!")


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


def sort_table(self, column, order):
    self.ui.articles_list.sortItems(column, order)

# Beispiel zum manuellen Einstellen der Spaltenbreite


def resize_columns_to_contents(self, list, columns):
    header = list.horizontalHeader()
    for i in range(columns):
        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
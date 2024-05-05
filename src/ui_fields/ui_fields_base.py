import os
from qtpy import QtWidgets

from odf.opendocument import load
from odf import text, teletype
from odf.table import Table, TableRow, TableCell

import files.logs_and_config as logs_and_config
import directories.directory_base as directory_base


def config_to_fields(self):
    try:
        #!################ Settings_Connection_Dialog ###########################

        self.sett_con_dlg.ui.db_server.setPlainText(
            logs_and_config.read_config_value(self, 'Server', 'server'))
        self.sett_con_dlg.ui.user.setPlainText(
            logs_and_config.read_config_value(self, 'Server', 'user'))
        self.sett_con_dlg.ui.pw.setPlainText(
            logs_and_config.read_config_value(self, 'Server', 'password'))
        self.sett_con_dlg.ui.db_name.setPlainText(
            logs_and_config.read_config_value(self, 'Server', 'dB_name'))
        self.sett_con_dlg.ui.query_input.setPlainText(
            logs_and_config.read_config_value(self, 'Abfrage', 'sql1'))
        self.sett_con_dlg.ui.query_2_input.setPlainText(
            logs_and_config.read_config_value(self, 'Abfrage', 'sql2'))

        #!################ Settings_Paths_Dialog ###########################

        self.sett_paths_dlg.ui.source_path_text.setPlainText(
            logs_and_config.read_config_value(self, 'Pfade', 'source_path'))
        self.sett_paths_dlg.ui.source_path_text_matstr.setPlainText(
            logs_and_config.read_config_value(self, 'Pfade', 'template1_path'))
        self.sett_paths_dlg.ui.source_path_text_docu.setPlainText(
            logs_and_config.read_config_value(self, 'Pfade', 'template2_path'))

        #!################ MainWindow ###########################

        self.ui.target_path_text.setPlainText(
            logs_and_config.read_config_value(self, 'Pfade', 'target_path'))
        self.ui.target_path_text_2.setPlainText(
            logs_and_config.read_config_value(self, 'Pfade', 'target_path_2'))

    except Exception as e:
        QtWidgets.QMessageBox.warning(
            self, "Fehler", f"Konfigurationsdaten konnten nicht geladen werden, daher wurde eine neue Konfigurationsdatei erstellt.\n\n"
            f"Fehlermeldung:\n {e}")
        config_path = directory_base.get_directories(self)['config_path']
        if os.path.exists(config_path):
            os.remove(config_path)
        logs_and_config.create_config_file(self)


def char_validation(self):
    textlength = 10
    # Speichere den vorherigen Text
    prev_string = self.previous_project_text
    current_string = self.ui.project.toPlainText()
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
        '{{module_type}}': (self.ui.module_type_text, aggr_dev_list(self.ui.PV_modules_list, 2)),
        '{{mounting_type}}': (self.ui.mounting_type_text, 'data_20'),
        '{{hybrid_inverter_bool}}': (self.ui.hybrid_inverter_bool_text, 'data_21'),
        '{{inverter_type}}': (self.ui.inverter_type_text, aggr_dev_list(self.ui.PV_inverters_list, 2)),
        '{{inverter_SN}}': (self.ui.inverter_SN_text, aggr_dev_list(self.ui.PV_inverters_list, 4)),
        '{{inverter_power}}': (self.ui.inverter_power_text, aggr_dev_list(self.ui.PV_inverters_list, 5)),
        '{{commiss_date}}': (self.ui.commiss_date_text, 'data_25'),
        '{{bat_inverter_type}}': (self.ui.bat_inverter_type_text, aggr_dev_list(self.ui.BAT_inverters_list, 2)),
        '{{bat_inverter_SN}}': (self.ui.bat_inverter_SN_text, aggr_dev_list(self.ui.BAT_inverters_list, 4)),
        '{{bat_inverter_power}}': (self.ui.bat_inverter_power_text, aggr_dev_list(self.ui.BAT_inverters_list, 5)),
        '{{coupling_type}}': (self.ui.coupling_type_text, aggr_dev_list(self.ui.BAT_inverters_list, 6)),
        '{{bat_storage_type}}': (self.ui.bat_storage_type_text, aggr_dev_list(self.ui.BAT_storage_list, 2)),
        '{{bat_storage_SN}}': (self.ui.bat_storage_SN_text, aggr_dev_list(self.ui.BAT_storage_list, 4)),
        '{{bat_storage_cap}}': (self.ui.bat_storage_cap_text, aggr_dev_list(self.ui.BAT_storage_list, 5)),
        '{{bat_commiss_date}}': (self.ui.bat_commiss_date_text, 'data_33'),
        '{{max_discharge_pow}}': (self.ui.max_discharge_pow_text, aggr_dev_list(self.ui.BAT_storage_list, 6)),
        '{{em_pow_ability_bool}}': (self.ui.em_pow_ability_bool_text, 'data_35'),
        '{{energy_storage_type}}': (self.ui.energy_storage_type_text, 'data_36'),
        '{{bat_technology}}': (self.ui.bat_technology_text, 'data_37'),
        '{{charging_point_type}}': (self.ui.charging_point_type_text, aggr_dev_list(self.ui.CHG_point_list, 2)),
        '{{charging_point_SN}}': (self.ui.charging_point_SN_text, aggr_dev_list(self.ui.CHG_point_list, 4)),
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


def aggr_dev_list(device_list, column_index):
    k = 1
    value = ''
    for row in range(device_list.rowCount()):
        if not device_list.item(row, column_index) == None:
            value = value + \
                f'{device_list.item(row, column_index).text()} ({str(k)})\n'
            k += 1
    value = value.rstrip('\n')
    return value


@directory_base.check_path_existence(modus=1)
def replace_fields_in_doc(self, doc_path, template_path):
    # Rufe get_directories auf, um die Pfade zu erhalten
    template = directory_base.get_directories(self)[
        template_path]
    doc = directory_base.get_directories(self)[
        doc_path]

    try:
        document = load(template)
        context = get_mapped_context(self)

        # Durchlaufe alle Tabellen in der ODF-Datei
        for table in document.getElementsByType(Table):
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

        document.save(doc)
        QtWidgets.QMessageBox.information(
            self, "Abgeschlossen!",
            f"Die Datei wurde unter folgendem Pfad gespeichert:\n"
            f"{doc}")

    except Exception as e:
        QtWidgets.QMessageBox.warning(
            self, "Fehler", f"Fehler bei der Feldersetzung: {e}")


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

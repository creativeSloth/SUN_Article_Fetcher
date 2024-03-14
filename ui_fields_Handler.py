import os
from qtpy import QtWidgets

import logs_and_config
import directory_Handler


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


def get_context(self):
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
        '{{inverter_type}}': (self.ui.inverter_type_text, 'data_22', 'default'),
        '{{inverter_SN}}': (self.ui.inverter_SN_text, 'data_23', 'default'),
        '{{inverter_power}}': (self.ui.inverter_power_text, 'data_24', 'default'),
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


def clear_docu_fields(self):
    [value[0].clear() for value in get_context(self).values()]

import logs_and_config


def set_field_inputs(self):
    self.project = self.ui.project.toPlainText()
    self.operator = self.ui.operator_text.toPlainText()
    self.op_adress_1 = self.ui.op_adress_1_text.toPlainText()
    self.op_adress_2 = self.ui.op_adress_2_text.toPlainText()
    self.op_adress_3 = self.ui.op_adress_3_text.toPlainText()
    self.loc_adress_1 = self.ui.loc_adress_1_text.toPlainText()
    self.loc_adress_2 = self.ui.loc_adress_2_text.toPlainText()
    self.loc_adress_3 = self.ui.loc_adress_3_text.toPlainText()
    self.sys_perf = self.ui.sys_perf_text.toPlainText()
    self.constr_style = self.ui.constr_style_text.toPlainText()
    self.bool_consist_azimuth = self.ui.bool_consist_azimuth_text.toPlainText()
    self.maj_azimuth = self.ui.maj_azimuth_text.toPlainText()
    self.maj_card_point = self.ui.maj_card_point_text.toPlainText()
    self.min_azimuth = self.ui.min_azimuth_text.toPlainText()
    self.min_card_point = self.ui.min_card_point_text.toPlainText()
    self.maj_tilt = self.ui.maj_tilt_text.toPlainText()
    self.min_tilt = self.ui.min_tilt_text.toPlainText()
    self.module_count = self.ui.module_count_text.toPlainText()
    self.module_type = self.ui.module_type_text.toPlainText()
    self.mounting_type = self.ui.mounting_type_text.toPlainText()
    self.hybrid_inverter_bool = self.ui.hybrid_inverter_bool_text.toPlainText()
    self.inverter_type = self.ui.inverter_type_text.toPlainText()
    self.inverter_SN = self.ui.inverter_SN_text.toPlainText()
    self.inverter_power = self.ui.inverter_power_text.toPlainText()
    self.commiss_date = self.ui.commiss_date_text.toPlainText()
    self.bat_inverter_type = self.ui.bat_inverter_type_text.toPlainText()
    self.bat_inverter_SN = self.ui.bat_inverter_SN_text.toPlainText()
    self.bat_inverter_power = self.ui.bat_inverter_power_text.toPlainText()
    self.coupling_type = self.ui.coupling_type_text.toPlainText()
    self.bat_storage_type = self.ui.bat_storage_type_text.toPlainText()
    self.bat_storage_SN = self.ui.bat_storage_SN_text.toPlainText()
    self.bat_storage_cap = self.ui.bat_storage_cap_text.toPlainText()
    self.bat_commiss_date = self.ui.bat_commiss_date_text.toPlainText()
    self.max_discharge_pow = self.ui.max_discharge_pow_text.toPlainText()
    self.em_pow_ability_bool = self.ui.em_pow_ability_bool_text.toPlainText()
    self.energy_storage_type = self.ui.energy_storage_type_text.toPlainText()
    self.bat_technology = self.ui.bat_technology_text.toPlainText()
    self.charging_point_type = self.ui.charging_point_type_text.toPlainText()
    self.charging_point_SN = self.ui.charging_point_SN_text.toPlainText()
    self.feeding_type = self.ui.feeding_type_text.toPlainText()
    self.pow_limit_bool = self.ui.pow_limit_bool_text.toPlainText()
    self.rmt_grd_op_bool = self.ui.rmt_grd_op_bool_text.toPlainText()
    self.rmt_drct_mrktr_bool = self.ui.rmt_drct_mrktr_bool_text.toPlainText()
    self.rmt_3rd_prt_bool = self.ui.rmt_3rd_prt_bool_text.toPlainText()
    self.prequali_bool = self.ui.prequali_bool_text.toPlainText()
    self.citizen_corp_bool = self.ui.citizen_corp_bool_text.toPlainText()
    self.tendering_bool = self.ui.tendering_bool_text.toPlainText()
    self.meter_cabinet = self.ui.meter_cabinet_text.toPlainText()
    self.meter_box_type = self.ui.meter_box_type_text.toPlainText()
    self.dl_type = self.ui.dl_type_text.toPlainText()
    self.dl_connect_ext = self.ui.dl_connect_ext_text.toPlainText()


def get_context(self):
    return {
        '{{project}}': self.project,
        '{{operator}}': self.operator,
        '{{op_adress_1}}': self.op_adress_1,
        '{{op_adress_2}}': self.op_adress_2,
        '{{op_adress_3}}': self.op_adress_3,
        '{{loc_adress_1}}': self.loc_adress_1,
        '{{loc_adress_2}}': self.loc_adress_2,
        '{{loc_adress_3}}': self.loc_adress_3,
        '{{sys_perf}}': self.sys_perf,
        '{{constr_style}}': self.constr_style,
        '{{bool_consist_azimuth}}': self.bool_consist_azimuth,
        '{{maj_azimuth}}': self.maj_azimuth,
        '{{maj_card_point}}': self.maj_card_point,
        '{{min_azimuth}}': self.min_azimuth,
        '{{min_card_point}}': self.min_card_point,
        '{{maj_tilt}}': self.maj_tilt,
        '{{min_tilt}}': self.min_tilt,
        '{{module_count}}': self.module_count,
        '{{module_type}}': self.module_type,
        '{{mounting_type}}': self.mounting_type,
        '{{hybrid_inverter_bool}}': self.hybrid_inverter_bool,
        '{{inverter_type}}': self.inverter_type,
        '{{inverter_SN}}': self.inverter_SN,
        '{{inverter_power}}': self.inverter_power,
        '{{commiss_date}}': self.commiss_date,
        '{{bat_inverter_type}}': self.bat_inverter_type,
        '{{bat_inverter_SN}}': self.bat_inverter_SN,
        '{{bat_inverter_power}}': self.bat_inverter_power,
        '{{coupling_type}}': self.coupling_type,
        '{{bat_storage_type}}': self.bat_storage_type,
        '{{bat_storage_SN}}': self.bat_storage_SN,
        '{{bat_storage_cap}}': self.bat_storage_cap,
        '{{bat_commiss_date}}': self.bat_commiss_date,
        '{{max_discharge_pow}}': self.max_discharge_pow,
        '{{em_pow_ability_bool}}': self.em_pow_ability_bool,
        '{{energy_storage_type}}': self.energy_storage_type,
        '{{bat_technology}}': self.bat_technology,
        '{{charging_point_type}}': self.charging_point_type,
        '{{charging_point_SN}}': self.charging_point_SN,
        '{{feeding_type}}': self.feeding_type,
        '{{pow_limit_bool}}': self.pow_limit_bool,
        '{{rmt_grd_op_bool}}': self.rmt_grd_op_bool,
        '{{rmt_drct_mrktr_bool}}': self.rmt_drct_mrktr_bool,
        '{{rmt_3rd_prt_bool}}': self.rmt_3rd_prt_bool,
        '{{prequali_bool}}': self.prequali_bool,
        '{{citizen_corp_bool}}': self.citizen_corp_bool,
        '{{tendering_bool}}': self.tendering_bool,
        '{{meter_cabinet}}': self.meter_cabinet,
        '{{meter_box_type}}': self.meter_box_type,
        '{{dl_type}}': self.dl_type,
        '{{dl_connect_ext}}': self.dl_connect_ext
    }


def config_to_fields(self):
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

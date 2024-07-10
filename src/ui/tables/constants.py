def set_general_table_map(self):

    self.GENERAL_TABLE_MAP = {
        self.ui.PV_modules_list: {
            "gui_open_bl_btn": self.ui.open_PV_modules_blacklist,
            "name_translated_german": "PV-Module",
            "db_bl_bool": "on_modules_bl",
            "db_added_to_bl_date": "added_to_modules_bl",
        },
        self.ui.PV_inverters_list: {
            "gui_open_bl_btn": self.ui.open_PV_inverters_blacklist,
            "name_translated_german": "PV-Wechselrichter",
            "db_bl_bool": "on_pv_inv_bl",
            "db_added_to_bl_date": "added_to_pv_inv_bl",
        },
        self.ui.BAT_inverters_list: {
            "gui_open_bl_btn": self.ui.open_BAT_inverters_blacklist,
            "name_translated_german": "Batterie-Wechselrichter",
            "db_bl_bool": "on_bat_inv_bl",
            "db_added_to_bl_date": "added_to_bat_inv_bl",
        },
        self.ui.BAT_storage_list: {
            "gui_open_bl_btn": self.ui.open_BAT_storage_blacklist,
            "name_translated_german": "Batterie-Speicher",
            "db_bl_bool": "on_bat_bl",
            "db_added_to_bl_date": "added_to_bat_bl",
        },
        self.ui.CHG_point_list: {
            "gui_open_bl_btn": self.ui.open_CHG_point_blacklist,
            "name_translated_german": "Ladestation",
            "db_bl_bool": "on_chg_point_bl",
            "db_added_to_bl_date": "added_to_chg_point_bl",
        },
        self.ui.articles_list: {
            "gui_open_bl_btn": self.ui.open_articles_blacklist,
            "name_translated_german": "Allgemeine Artikel",
            "db_bl_bool": "on_articles_bl",
            "db_added_to_bl_date": "added_to_articles_bl",
        },
    }

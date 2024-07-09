BLACKLISTS = []
BLACKLISTS_TABLE_MAP = []


def get_blacklist_map(self):

    button_dict = {
        "PV_modules_list": (self.ui.open_PV_modules_blacklist, "PV-Module"),
        "PV_inverters_list": (self.ui.open_PV_inverters_blacklist, "PV-Wechselrichter"),
        "BAT_inverters_list": (
            self.ui.open_BAT_inverters_blacklist,
            "Batterie-Wechselrichter",
        ),
        "BAT_storage_list": (self.ui.open_BAT_storage_blacklist, "Batterie-Speicher"),
        "CHG_point_list": (self.ui.open_CHG_point_blacklist, "Ladestation"),
        "articles_list": (self.ui.open_articles_blacklist, "Allgemeine Artikel"),
    }

    return button_dict

SOURCE = "source_path"
TARGET_1 = "target_1_path"
TEMPLATE_1 = "template_1_path"
DOC_1 = "doc_1_path"
TARGET_2 = "target_2_path"
TEMPLATE_2 = "template_2_path"
DOC_2 = "doc_2_path"

LOG_SUBF = "log_subfolder_path"
LOG_SUBF_2 = "log_subfolder_2_path"
CONFIG = "config_path"
BLACKLISTS = "blacklist_path"
DB = "SUN_DOC_db_path"
DEVICE_SPECS = "device_specs_list_path"
STYLESHEET = "stylesheet_path"
ICONS_FOLDER = "icons_folder_path"

DOC_1_NAME = "Doku - Anlagendaten für MaStR"
DOC_2_NAME = "Doku NIO - SQL Adressen V1.0"

LOG_SUBF_NAME = "logs"
LOG_SUBF_2_NAME = "hist"
CONFIG_NAME = "config.ini"
BLACKLISTS_NAME = "blacklists.ini"
DB_NAME = "SUN_DOC_DB.db"
DEVICE_SPECS_NAME = "device_specs_list.ini"
STYLESHEETF_NAME = "styles"
STYLESHEET_NAME = "stylesheet.qss"
ICONSSUPERF_NAME = "ui"

ICONSF_NAME = "icons"


class Paths:
    def __init__(self):
        self.paths = {
            SOURCE: "",
            TARGET_1: "",
            TEMPLATE_1: "",
            DOC_1: "",
            TARGET_2: "",
            TEMPLATE_2: "",
            DOC_2: "",
            LOG_SUBF: "",
            LOG_SUBF_2: "",
            CONFIG: "",
            # BLACKLISTS: "",
            DB: "",
            # DEVICE_SPECS: "",
            STYLESHEET: "",
            ICONS_FOLDER: "",
        }

    def set_path(self, key, value):
        if key in self.paths:
            # Umformung des Strings: Alle Backslashes zu Slashes
            self.paths[key] = value.replace("\\", "/")
        else:
            raise KeyError(f"Key '{key}' does not exist in the paths dictionary.")

    def get_path(self, key):
        if key in self.paths:
            return self.paths[key]
        else:
            raise KeyError(f"Key '{key}' does not exist in the paths dictionary.")


DIRS: Paths = Paths()

class Paths:
    def __init__(self):
        self.dict = {
            "source_path": "",
            "target_1_path": "",
            "template_1_path": "",
            "doc_1_path": "",
            "target_2_path": "",
            "template_2_path": "",
            "doc_2_path": "",
            "log_subfolder_path": "",
            "log_subfolder_2_path": "",
            "config_path": "",
            "blacklist_path": "",
            "blacklist_db_path": "",
            "device_specs_list_path": "",
            "stylesheet_path": "",
            "icons_folder_path": "",
        }

    def set_path(self, key, value):
        if key in self.dict:
            # Umformung des Strings: Alle Backslashes zu Slashes
            self.dict[key] = value.replace("\\", "/")
        else:
            raise KeyError(f"Key '{key}' does not exist in the paths dictionary.")

    def get_path(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            raise KeyError(f"Key '{key}' does not exist in the paths dictionary.")


dir_paths: Paths = Paths()

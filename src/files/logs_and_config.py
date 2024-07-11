import configparser
import os
from datetime import datetime

from PyQt5.QtWidgets import QMessageBox

import directories.constants
import directories.document_helpers as directory_base


def create_config_file():
    config_path = directories.constants.dir_paths.dict["config_path"]

    if os.path.exists(config_path):
        return

    config = configparser.ConfigParser()

    # Fülle die Konfiguration mit Standardwerten
    config["Pfade"] = {
        "source_path": "",
        "target_1_path": "",
        "template_1_path": "",
        "template_2_path": "",
        "target_2_path": "",
        "config_path": config_path,
    }

    config["Abfrage"] = {"sql1": "", "sql2": ""}
    config["Server"] = {"server": "", "user": "", "password": "", "dB_name": ""}

    # Schreibe die Konfiguration in die Datei
    with open(config_path, "w") as configfile:
        config.write(configfile)


def create_save_file(self):
    file_path = directory_base.set_save_file_dir(self)

    if file_path != "":
        save_file = configparser.ConfigParser()
        save_file["Fields text"] = {}
        save_file["Tables content"] = {}

        with open(file_path, "w") as savefile:
            save_file.write(savefile)
    return file_path


def update_save_file(field_map, file_path, section):
    if file_path:
        save_file = configparser.ConfigParser()

        if os.path.exists(file_path):
            save_file.read(file_path)

        for field in field_map:
            save_file.set(section, str(field[0]), str(field[1]))

        with open(file_path, "w") as savefile:
            save_file.write(savefile)


def load_save_file(file_path, section):
    save_file = configparser.ConfigParser()
    save_file.read(file_path)
    saved_field_values = {}
    if save_file.has_section(section):
        for option in save_file[section]:
            saved_field_values[option] = save_file[section][option]
    return saved_field_values


def update_config_file(section, option, value):
    config_path = directories.constants.dir_paths.dict["config_path"]
    config = configparser.ConfigParser()
    config.read(config_path)
    config[section][option] = value

    with open(config_path, "w") as configfile:
        config.write(configfile)


def read_config_value(section, option):
    config_path = directories.constants.dir_paths.dict["config_path"]
    config = configparser.ConfigParser()
    config.read(config_path)
    value = config[section][option]
    return value


def log_copy_details(self, source_path, target_path, source_files, matching_files, df):
    # Erstelle einen Zeitstempel für die Log-Datei
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    log_source_file_name = f"datalog_{timestamp}.txt"

    log_subfolder_2_path = directories.constants.dir_paths.dict["log_subfolder_2_path"]

    # Pfad zur Log-Datei im Unterordner "logs"
    log_file_path = os.path.join(log_subfolder_2_path, log_source_file_name)

    # Öffne die Log-Datei für das Schreiben
    with open(log_file_path, "w", encoding="utf-8") as log_file:
        # Schreibe die Quell- und Zielordner in die Log-Datei
        log_file.write(f"Source Folder: {source_path}\n")
        log_file.write(f"Target Folder: {target_path}\n\n")

        # Schreibe alle Dateinamen im source_path in die Log-Datei
        log_file.write("All Files in Source Folder:\n")
        for file in source_files:
            try:
                # Kodiere den Dateinamen als UTF-8, um sicherzustellen, dass Sonderzeichen korrekt verarbeitet werden
                file_encoded = file.encode("utf-8", errors="ignore").decode("utf-8")
                log_file.write(f"- {file_encoded}\n")
            except Exception as e:
                QMessageBox.warning(
                    self,
                    "Fehler!",
                    f"Die Datei '{file}' des Quellordners konnte nicht in der log-datei registriert werden.\n\n {e}",
                )
        log_file.write("\n")

        # Schreibe die ausgewählten Dokumente in die Log-Datei
        log_file.write("Selected documents:\n")
        for file in matching_files:
            try:
                # Kodiere den Dateinamen als UTF-8, um sicherzustellen, dass Sonderzeichen korrekt verarbeitet werden
                file_encoded = file.encode("utf-8", errors="ignore").decode("utf-8")
                log_file.write(f"- {file_encoded}\n")
            except Exception as e:
                QMessageBox.warning(
                    self,
                    "Fehler!",
                    f"Die passende Datei '{file}' des Zielordner konnte nicht in der log-datei registriert werden.\n\n {e}",
                )
        log_file.write("\n")

        # Schreibe das DataFrame in die Log-Datei
        log_file.write("\nDataFrame from File or Database:\n")
        if df is not None:
            log_file.write(df.to_csv(index=False))


def create_device_related_storage_list(storage_file: str = None):
    related_path = directories.constants.dir_paths.dict[storage_file]

    if os.path.exists(related_path):
        return
    config = configparser.ConfigParser()

    # Schreibe die Konfiguration in die Datei
    with open(related_path, "w") as related_file:
        config.write(related_file)


def update_device_related_storage_list(storage_file, data_set):
    file_path = directories.constants.dir_paths.dict[storage_file]
    store_file = configparser.ConfigParser()

    # Lade vorhandene Konfiguration, wenn die Datei vorhanden ist
    if os.path.exists(storage_file):
        store_file.read(storage_file)

    for section, option, value in data_set:
        # Erstellen Sie die Sektion, wenn sie noch nicht existiert
        if not store_file.has_section(section):
            store_file.add_section(section)

        option = change_str_to_config_format(option)

        # Fügen den Wert unter der gegebenen Sektion und option hinzu
        store_file.set(section, option, value)

    with open(file_path, "w") as file:
        store_file.write(file)


def read_device_related_storage_list(storage_file, section, option):
    file_path = directories.constants.dir_paths.dict[storage_file]

    stored_file = configparser.ConfigParser()
    stored_file.read(file_path)
    # Überprüfen Sie, ob die angegebene Sektion vorhanden ist
    if stored_file.has_section(section):
        option = change_str_to_config_format(option)
        if stored_file.has_option(section, option):
            value = stored_file[section][option]
            if value is not None and value != "":
                return value
            return None


def change_str_to_config_format(string):
    string = string.replace("[", "<")
    string = string.replace("]", ">")
    string = string.replace("\n", "")
    return string

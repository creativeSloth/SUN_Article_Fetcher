import configparser
from fileinput import filename
import os
from datetime import datetime
from qtpy import QtWidgets

import directory_Handler


def create_config_file(self):
    config_path = directory_Handler.get_directories(self)['config_path']

    if os.path.exists(config_path):
        return

    config = configparser.ConfigParser()

    # Fülle die Konfiguration mit Standardwerten
    config['Pfade'] = {
        'source_path': '',
        'target_path': '',
        'template1_path': '',
        'template2_path': '',
        'target_path_2': '',
        'config_path': config_path
    }

    config['Abfrage'] = {
        'sql1': '',
        'sql2': ''
    }
    config['Server'] = {
        'server': '',
        'user': '',
        'password': '',
        'dB_name': ''
    }

    # Schreibe die Konfiguration in die Datei
    with open(config_path, 'w') as configfile:
        config.write(configfile)


def update_config_file(self, section, option, value):
    config_path = directory_Handler.get_directories(self)['config_path']
    config = configparser.ConfigParser()
    config.read(config_path)
    config[section][option] = value

    with open(config_path, 'w') as configfile:
        config.write(configfile)


def read_config_value(self, section, option):
    config_path = directory_Handler.get_directories(self)['config_path']
    config = configparser.ConfigParser()
    config.read(config_path)
    value = config[section][option]
    return value


def log_copy_details(self, source_path, target_path, source_files, matching_files, df):
    # Erstelle einen Zeitstempel für die Log-Datei
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    log_source_file_name = f"datalog_{timestamp}.txt"

    # Erstelle den Unterordner, falls er noch nicht existiert
    directory_Handler.set_directories(self)

    log_sub2folder_path = directory_Handler.get_directories(self)[
        'log_sub2folder_path']

    # Pfad zur Log-Datei im Unterordner "logs"
    log_file_path = os.path.join(
        log_sub2folder_path, log_source_file_name)

    # Öffne die Log-Datei für das Schreiben
    with open(log_file_path, 'w', encoding='utf-8') as log_file:
        # Schreibe die Quell- und Zielordner in die Log-Datei
        log_file.write(f"Source Folder: {source_path}\n")
        log_file.write(f"Target Folder: {target_path}\n\n")

        # Schreibe alle Dateinamen im source_path in die Log-Datei
        log_file.write("All Files in Source Folder:\n")
        for file in source_files:
            try:
                # Kodiere den Dateinamen als UTF-8, um sicherzustellen, dass Sonderzeichen korrekt verarbeitet werden
                file_encoded = file.encode(
                    'utf-8', errors='ignore').decode('utf-8')
                log_file.write(f"- {file_encoded}\n")
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Fehler!",
                                              f"Die Datei '{file}' des Quellordners konnte nicht in der log-datei registriert werden.\n\n {e}")
        log_file.write("\n")

        # Schreibe die ausgewählten Dokumente in die Log-Datei
        log_file.write("Selected documents:\n")
        for file in matching_files:
            try:
                # Kodiere den Dateinamen als UTF-8, um sicherzustellen, dass Sonderzeichen korrekt verarbeitet werden
                file_encoded = file.encode(
                    'utf-8', errors='ignore').decode('utf-8')
                log_file.write(f"- {file_encoded}\n")
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Fehler!",
                                              f"Die passende Datei '{file}' des Zielordner konnte nicht in der log-datei registriert werden.\n\n {e}")
        log_file.write("\n")

        # Schreibe das DataFrame in die Log-Datei
        log_file.write("\nDataFrame from File or Database:\n")
        if df is not None:
            log_file.write(df.to_csv(index=False))

#! Vllt die folgende Funktion mit "update_device_related_storage_list()" vereinen?


def update_blacklist(self, df, list):
    blacklist_path = directory_Handler.get_directories(self)['blacklist_path']

    config = configparser.ConfigParser()

    # Lade vorhandene Konfiguration, wenn die Datei vorhanden ist
    if os.path.exists(blacklist_path):
        config.read(blacklist_path)

    # Erstellen Sie die Sektion, wenn sie noch nicht existiert
    if not config.has_section(list):
        config.add_section(list)

    # Überprüfen, ob Artikel bereits vorhanden sind, und nur neue hinzufügen
    existing_articles = set(config.options(list))
    for _, row in df.iterrows():
        article_no = row['article_no']
        article_name = row['article_name']
        if article_no not in existing_articles:
            # Fügen Sie die Daten als Optionen unter der gegebenen Sektion hinzu
            config.set(list, article_no, article_name)

    # Schreibe die aktualisierte Konfiguration in die Datei
    with open(blacklist_path, 'w') as blacklist_file:
        config.write(blacklist_file)


def read_blacklist_article_numbers(self, list_name):
    blacklist_path = directory_Handler.get_directories(self)['blacklist_path']
    config = configparser.ConfigParser()
    config.read(blacklist_path)
    # Überprüfen Sie, ob die angegebene Sektion vorhanden ist
    article_numbers = []
    if config.has_section(list_name):
        # Holen Sie sich alle Schlüssel-Wert-Paare in der Sektion
        article_numbers = [str(key) for key, _ in config.items(list_name)]

    return article_numbers


def create_device_related_storage_list(self, storage_file=None):
    related_path = directory_Handler.get_directories(self)[storage_file]

    if os.path.exists(related_path):
        return
    config = configparser.ConfigParser()

    # Schreibe die Konfiguration in die Datei
    with open(related_path, 'w') as related_file:
        config.write(related_file)


def update_device_related_storage_list(self, storage_file, data_set):
    file_path = directory_Handler.get_directories(self)[storage_file]
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

    with open(file_path, 'w') as file:
        store_file.write(file)


def read_device_related_storage_list(self, storage_file, section, option):
    file_path = directory_Handler.get_directories(
        self)[storage_file]

    store_file = configparser.ConfigParser()
    store_file.read(file_path)
    # Überprüfen Sie, ob die angegebene Sektion vorhanden ist
    print(option)
    if store_file.has_section(section):
        option = change_str_to_config_format(option)
        if store_file.has_option(section, option):
            value = store_file[section][option]
            if value is not None and value != '':
                return value
            return None


def change_str_to_config_format(string):
    string = string.replace('[', '<')
    string = string.replace(']', '>')
    string = string.replace('\n', 'chr(13)')
    return string

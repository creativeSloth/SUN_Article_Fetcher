import configparser
import os
from datetime import datetime
from qtpy import QtWidgets

import directory_Handler


def create_config_file(filename):
    config = configparser.ConfigParser()

    # Fülle die Konfiguration mit Standardwerten
    config['Pfade'] = {
        'source_path': '',
        'target_path': '',
        'template1_path': '',
        'template2_path': '',
        'target_path_2': ''
    }

    config['Abfrage'] = {
        'sql1': '',
        'sql2': ''
    }
    config['Server'] = {
        'server': '',
        'user': '',
        'password': '',
        'DB-name': ''
    }

    # Schreibe die Konfiguration in die Datei
    with open(filename, 'w') as configfile:
        config.write(configfile)


def log_copy_details(self, source_path, target_path, source_files, matching_files):
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
        if self.df is not None:
            log_file.write(self.df.to_csv(index=False))

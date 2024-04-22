import os
import sys
from datetime import datetime

from functools import wraps

from PyQt5.QtWidgets import QFileDialog
from qtpy import QtWidgets


def get_directories(self):
    project = self.ui.project.toPlainText()
    # Setze den dynamischen Pfad zur Log-Datei relativ zum Skript
    if getattr(sys, 'frozen', False):
        # Skript wird im gepackten Zustand ausgeführt
        script_dir = os.path.dirname(sys.executable)
    else:
        # Skript wird normal ausgeführt
        script_dir = os.path.dirname(os.path.abspath(__file__))
    # **************************  Article Fetcher module  ********************************************

    source_path = self.ui.source_path_text.toPlainText()
    target_path_1 = self.ui.target_path_text.toPlainText()

    # **************************  Documentation module  **********************************************

    current_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    doc1_name = f"{project} Doku - Anlagendaten für MaStR {current_date}.odt"
    doc2_name = f"{project} Doku NIO - SQL Adressen V1.0 {current_date}.odt"
    target_path_2 = self.ui.target_path_text_2.toPlainText()

    # ? **********************************************************************************************
    # Ziehen der Dateipfade aus den Textfeldern
    template1_path = self.ui.source_path_text_matstr.toPlainText()
    doc1_path = os.path.join(target_path_2, doc1_name)

    template2_path = self.ui.source_path_text_docu.toPlainText()
    doc2_path = os.path.join(target_path_2, doc2_name)

    # ***************************  Config and LOGGING  **********************************************************

    # Pfad zum Unterordner "logs"
    log_subfolder_path = os.path.join(script_dir, "logs")
    log_sub2folder_path = os.path.join(
        log_subfolder_path, "hist")
    # Pfad zur Config
    config_path = os.path.join(log_subfolder_path, 'config.ini')
    # Pfad zur Config
    blacklist_path = os.path.join(log_subfolder_path, 'blacklist.ini')
    device_specs_list_path = os.path.join(
        log_subfolder_path, 'device_specs_list.ini')

    # ************************************************************************************************

    paths_dict = {
        'source_path': source_path,
        'target_path_1': target_path_1,
        'template1_path': template1_path,
        'doc1_path': doc1_path,
        'target_path_2': target_path_2,
        'template2_path': template2_path,
        'doc2_path': doc2_path,
        'log_subfolder_path': log_subfolder_path,
        'log_sub2folder_path': log_sub2folder_path,
        'config_path': config_path,
        'blacklist_path': blacklist_path,
        'device_specs_list_path': device_specs_list_path
    }

    return paths_dict


def set_directories(self):
    log_subfolder_path = get_directories(self)['log_subfolder_path']
    log_sub2folder_path = get_directories(self)['log_sub2folder_path']
    os.makedirs(log_subfolder_path, exist_ok=True)
    os.makedirs(log_sub2folder_path, exist_ok=True)


def set_save_file_dir(self):
    file_path, _ = QFileDialog.getSaveFileName(
        self, "Datei speichern", "", "Save files (*.sav)")
    return file_path


def get_save_file_dir(self):
    file_path, _ = QFileDialog.getOpenFileName(
        self, "Datei laden", "", "Save files (*.sav)")

    return file_path


# *********************************  Decorators  *************************************


def get_file_path(func):
    @wraps(func)
    def wrapper(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Wähle die Datei aus!")
        if file_path:
            func(self, file_path)
    return wrapper


def get_folder_path(func):
    @wraps(func)
    def wrapper(self):
        folder_path = QFileDialog.getExistingDirectory(
            self, "Wähle den Ordner aus!")
        if folder_path:
            func(self, folder_path)
    return wrapper


def check_path_existence(modus):
    def sub_check_path_existence(func):
        def wrapper(self, *args, **kwargs):

            paths_dict = get_directories(self)
            source_path = paths_dict['source_path']
            target_path_1 = paths_dict['target_path_1']
            template1_path = paths_dict['template1_path']
            target_path_2 = paths_dict['target_path_2']
            template2_path = paths_dict['template2_path']

            paths_and_messages = [
                (source_path, "Quellpfad existiert nicht."),
                (target_path_1, "Zielpfad existiert nicht."),
                (template1_path, "Template (Anlagendatenblatt gem. MatStR) existiert nicht unter angegebenen Pfad."),
                (target_path_2, "Ablagepfad existiert nicht oder wurde nicht ausgewählt."),
                (template2_path, "Template (Dokumentation) existiert nicht unter angegebenen Pfad.")
            ]

            files_and_messages = [
                (template1_path, "Es ist kein Template (Anlagendatenblatt gem. MatStR) ausgewählt worden."),
                (template2_path, "Es ist kein Template (Dokumentation) ausgewählt worden."),
            ]

            if modus == 0:
                for path, message in paths_and_messages[:2]:
                    if not os.path.exists(path):
                        QtWidgets.QMessageBox.warning(
                            self, "Fehler", message)
                        return

            if modus == 1:
                for path, message in paths_and_messages[2:]:
                    # ! "and message != paths_and_messages[2][1]" kann entfernt werden, wenn template2_path genutzt wird
                    # ! und das Loggen von allen Pfaden in einer zentralen ini-Datei geregelt wird
                    if not os.path.exists(path) and message != paths_and_messages[4][1]:

                        QtWidgets.QMessageBox.warning(
                            self, "Fehler", message)
                        return

                for file, message in files_and_messages:
                    # ! ebenso
                    if not os.path.isfile(file) and message != files_and_messages[1][1]:
                        QtWidgets.QMessageBox.warning(self, "Fehler", message)
                        return

            return func(self, *args, **kwargs)
        return wrapper
    return sub_check_path_existence

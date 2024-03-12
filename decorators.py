
import os
from functools import wraps

from PyQt5.QtWidgets import QFileDialog
from qtpy import QtWidgets


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
            source_path, target_path, template1_path, _, template2_path, _, target_path_2 = self.get_directories()

            paths_and_messages = [
                (source_path, "Quellpfad existiert nicht."),
                (target_path, "Zielpfad existiert nicht."),
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

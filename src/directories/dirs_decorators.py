import os

from PyQt5.QtWidgets import QFileDialog, QMessageBox

from directories.constants import dir_paths


def get_folder_path(func):
    def wrapper(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Wähle den Ordner aus!")
        if folder_path:
            func(self, folder_path)

    return wrapper


def get_file_path(func):
    def wrapper(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Wähle die Datei aus!")
        if file_path:
            func(self, file_path)

    return wrapper


def check_path_existence(modus):
    def sub_check_path_existence(func):
        def wrapper(self, *args, **kwargs):

            source_path = dir_paths.dict["source_path"]
            target_1_path = dir_paths.dict["target_1_path"]
            template_1_path = dir_paths.dict["template_1_path"]
            target_2_path = dir_paths.dict["target_2_path"]
            template_2_path = dir_paths.dict["template_2_path"]

            paths_and_messages = [
                (source_path, "Quellpfad existiert nicht."),
                (target_1_path, "Zielpfad existiert nicht."),
                (
                    template_1_path,
                    "Template (Anlagendatenblatt gem. MatStR) existiert nicht unter angegebenen Pfad.",
                ),
                (
                    target_2_path,
                    "Ablagepfad existiert nicht oder wurde nicht ausgewählt.",
                ),
                (
                    template_2_path,
                    "Template (Dokumentation) existiert nicht unter angegebenen Pfad.",
                ),
            ]

            files_and_messages = [
                (
                    template_1_path,
                    "Es ist kein Template (Anlagendatenblatt gem. MatStR) ausgewählt worden.",
                ),
                (
                    template_2_path,
                    "Es ist kein Template (Dokumentation) ausgewählt worden.",
                ),
            ]

            if modus == 0:
                for path, message in paths_and_messages[:2]:
                    if not os.path.exists(path):
                        QMessageBox.warning(self, "Fehler", message)
                        return

            if modus == 1:
                for path, message in paths_and_messages[2:]:
                    # ! "and message != paths_and_messages[2][1]" kann entfernt werden, wenn template2_path genutzt wird
                    # ! und das Loggen von allen Pfaden in einer zentralen ini-Datei geregelt wird
                    if not os.path.exists(path) and message != paths_and_messages[4][1]:

                        QMessageBox.warning(self, "Fehler", message)
                        return

                for file, message in files_and_messages:
                    # ! ebenso
                    if not os.path.isfile(file) and message != files_and_messages[1][1]:
                        QMessageBox.warning(self, "Fehler", message)
                        return

            return func(self, *args, **kwargs)

        return wrapper

    return sub_check_path_existence

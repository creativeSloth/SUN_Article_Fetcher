import inspect
import os
import sys
from datetime import datetime

from PyQt5.QtWidgets import QFileDialog, QMessageBox


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
            "device_specs_list_path": "",
            "stylesheet_path": "",
            "icons_folder_path": "",
        }


dir_paths: Paths = Paths()


def set_static_directories():

    (
        log_subfolder_path,
        log_subfolder_2_path,
        config_path,
        blacklist_path,
        device_specs_list_path,
        stylesheet_path,
        icons_folder_path,
    ) = create_static_dirs()
    # **************************  Article Fetcher module  ********************************************

    # Setze die Pfade direkt im dict-Attribut der _main_paths Instanz
    dir_paths.dict["log_subfolder_path"] = log_subfolder_path
    dir_paths.dict["log_subfolder_2_path"] = log_subfolder_2_path
    dir_paths.dict["config_path"] = config_path
    dir_paths.dict["blacklist_path"] = blacklist_path
    dir_paths.dict["device_specs_list_path"] = device_specs_list_path
    dir_paths.dict["stylesheet_path"] = stylesheet_path
    dir_paths.dict["icons_folder_path"] = icons_folder_path


def get_main_dir():

    # Finde das Verzeichnis, in dem main.py liegt
    main_script_path = inspect.getsourcefile(sys.modules["__main__"])
    main_script_dir = os.path.dirname(main_script_path)

    # Setze den dynamischen Pfad zur Log-Datei relativ zum Verzeichnis von main.py
    if getattr(sys, "frozen", False):
        # Skript wird im gepackten Zustand ausgeführt
        script_dir = os.path.dirname(sys.executable)
    else:
        # Skript wird normal ausgeführt
        script_dir = main_script_dir

    return script_dir


def create_static_dirs():
    log_subfolder_path, log_subfolder_2_path = create_log_subfolders()
    (
        config_path,
        blacklist_path,
        device_specs_list_path,
        stylesheet_path,
        icons_folder_path,
    ) = create_storage_files(log_subfolder_path)
    return (
        log_subfolder_path,
        log_subfolder_2_path,
        config_path,
        blacklist_path,
        device_specs_list_path,
        stylesheet_path,
        icons_folder_path,
    )


def create_log_subfolders():
    script_dir = get_main_dir()
    # Pfad zum Unterordner "logs"
    log_subfolder_path = os.path.join(script_dir, "logs")
    os.makedirs(log_subfolder_path, exist_ok=True)
    log_subfolder_2_path = os.path.join(log_subfolder_path, "hist")
    os.makedirs(log_subfolder_2_path, exist_ok=True)
    return log_subfolder_path, log_subfolder_2_path


def create_storage_files(log_path):
    script_dir = get_main_dir()
    # Pfad zur Config
    config_path = os.path.join(log_path, "config.ini")
    # Pfad zur blacklist
    blacklist_path = os.path.join(log_path, "blacklist.ini")
    device_specs_list_path = os.path.join(log_path, "device_specs_list.ini")
    stylesheet_path = os.path.join(script_dir, "styles", "stylesheet.qss")
    icons_folder_path = os.path.join(script_dir, "ui", "icons")
    return (
        config_path,
        blacklist_path,
        device_specs_list_path,
        stylesheet_path,
        icons_folder_path,
    )


def set_source_dir(dir):
    dir_paths.dict["source_path"] = dir


def set_target_1_dir(dir):
    dir_paths.dict["target_1_path"] = dir


def set_target_2_dir(dir):
    dir_paths.dict["target_2_path"] = dir


def set_template_dir(template, dir):
    dir_paths.dict[template] = dir


def set_doc_1_dir(self):
    doc_1, _ = get_docs_paths(project=self.ui.project.toPlainText())
    dir_paths.dict["doc_1_path"] = doc_1


def set_doc_2_dir(self):
    doc_2, _ = get_docs_paths(project=self.ui.project.toPlainText())
    dir_paths.dict["doc_2_path"] = doc_2


def get_docs_paths(project):
    target_2_path = dir_paths.dict["target_2_path"]
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    doc1_name = f"{project} - Doku - Anlagendaten für MaStR - {timestamp}.odt"
    doc2_name = f"{project} - Doku NIO - SQL Adressen V1.0 - {timestamp}.odt"
    doc_1 = os.path.join(target_2_path, doc1_name)
    doc_2 = os.path.join(target_2_path, doc2_name)
    return doc_1, doc_2

    # ************************************************************************************************


def set_save_file_dir(self):
    file_path, _ = QFileDialog.getSaveFileName(
        self, "Datei speichern", "", "Save files (*.sav)"
    )
    return file_path


def get_save_file_dir(self):
    file_path, _ = QFileDialog.getOpenFileName(
        self, "Datei laden", "", "Save files (*.sav)"
    )

    return file_path


# *********************************  Decorators  *************************************


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

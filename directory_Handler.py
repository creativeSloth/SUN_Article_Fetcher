import os
import sys
from datetime import datetime


def get_directories(self):
    project = self.get_project()
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
    # Pfad zur Config
    config_path = os.path.join(script_dir, 'config.ini')
    # Pfad zum Unterordner "logs"
    log_subfolder_path = os.path.join(script_dir, "logs")
    log_sub2folder_path = os.path.join(
        log_subfolder_path, "hist")

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
        'config_path': config_path
    }

    return paths_dict


def set_directories(self):
    log_subfolder_path = get_directories(self)['log_subfolder_path']
    log_sub2folder_path = get_directories(self)['log_sub2folder_path']
    os.makedirs(log_subfolder_path, exist_ok=True)
    os.makedirs(log_sub2folder_path, exist_ok=True)

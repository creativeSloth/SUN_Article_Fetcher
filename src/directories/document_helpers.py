import os
from datetime import datetime

from PyQt5.QtWidgets import QFileDialog

from directories.constants import dir_paths


def get_docs_paths(project):
    target_2_path = dir_paths.dict["target_2_path"]
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    doc1_name = f"{project} - Doku - Anlagendaten für MaStR - {timestamp}.odt"
    doc2_name = f"{project} - Doku NIO - SQL Adressen V1.0 - {timestamp}.odt"
    doc_1 = os.path.join(target_2_path, doc1_name)
    doc_2 = os.path.join(target_2_path, doc2_name)
    return doc_1, doc_2


def set_doc_2_dir(self):
    doc_2, _ = get_docs_paths(project=self.ui.project.toPlainText())
    dir_paths.dict["doc_2_path"] = doc_2


def set_doc_1_dir(self):
    doc_1, _ = get_docs_paths(project=self.ui.project.toPlainText())
    dir_paths.dict["doc_1_path"] = doc_1


def set_source_dir(dir):
    dir_paths.dict["source_path"] = dir


def set_target_1_dir(dir):
    dir_paths.dict["target_1_path"] = dir


def set_target_2_dir(dir):
    dir_paths.dict["target_2_path"] = dir


def set_template_dir(template, dir):
    dir_paths.dict[template] = dir


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

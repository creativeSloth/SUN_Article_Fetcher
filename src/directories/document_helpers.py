import os
from datetime import datetime

from PyQt5.QtWidgets import QFileDialog

from directories.constants import (
    DIRS,
    DOC_1,
    DOC_1_NAME,
    DOC_2,
    DOC_2_NAME,
    SOURCE,
    TARGET_1,
    TARGET_2,
)


def get_docs_paths(project):
    target_2_path = DIRS.paths[TARGET_2]
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    doc1_name = f"{project} - {DOC_1_NAME} - {timestamp}.odt"
    doc2_name = f"{project} - {DOC_2_NAME} - {timestamp}.odt"
    doc_1 = os.path.join(target_2_path, doc1_name)
    doc_2 = os.path.join(target_2_path, doc2_name)
    return doc_1, doc_2


def set_doc_1_dir(self):
    doc_1, _ = get_docs_paths(project=self.ui.project.toPlainText())
    DIRS.paths[DOC_1] = doc_1


def set_doc_2_dir(self):
    doc_2, _ = get_docs_paths(project=self.ui.project.toPlainText())
    DIRS.paths[DOC_2] = doc_2


def set_source_dir(dir):
    DIRS.paths[SOURCE] = dir


def set_target_1_dir(dir):
    DIRS.paths[TARGET_1] = dir


def set_target_2_dir(dir):
    DIRS.paths[TARGET_2] = dir


def set_template_dir(template, dir):
    DIRS.paths[template] = dir


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

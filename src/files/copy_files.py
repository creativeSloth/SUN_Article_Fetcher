import os
import shutil

import pandas as pd
from PyQt5.QtGui import QFont
from qtpy import QtCore, QtWidgets

import directories.directory_base as directory_base
import files.logs_and_config as logs_and_config


def get_paths(self):
    source_path = directory_base.get_directories(self)['source_path']
    target_path = directory_base.get_directories(self)['target_path_1']
    log_sub2folder_path = directory_base.get_directories(self)[
        'log_sub2folder_path']
    return source_path, target_path, log_sub2folder_path


def get_selected_files_and_df(self):
    selected_files = []
    df = pd.DataFrame(columns=['article_no', 'article_name', 'count'])
    table = self.ui.articles_list

    for row in range(table.rowCount()):
        checkbox_item = table.item(row, 0)
        article_no = table.item(row, 1).text()
        article_name = table.item(row, 2).text()

        new_data = pd.DataFrame(
            {'article_no': [article_no],
             'article_name': [article_name]
             })

        df = pd.concat([df, new_data], ignore_index=True)

        if checkbox_item and checkbox_item.checkState() == QtCore.Qt.Checked:
            selected_files.append(article_no)

    selected_files = list(set(selected_files))
    return selected_files, df


def get_matching_files(source_files, selected_files):
    return [file for file in source_files
            if any(selected_file in file for selected_file in selected_files)]


def mark_matching_files(self, matching_files):
    table = self.ui.articles_list
    for row in range(table.rowCount()):
        article_no_item = table.item(row, 1)
        article_no = article_no_item.text()

        if any(article_no in matching_file for matching_file in matching_files):
            font = QFont()
            font.setBold(True)
            article_no_item.setFont(font)


def copy_files(self, matching_files, source_path, target_path):
    count = 0
    table = self.ui.articles_list

    for matching_filename in matching_files:
        source_file_path = os.path.join(source_path, matching_filename)
        target_file_path = os.path.join(target_path, matching_filename)
        target_file_path_ext = os.path.dirname(target_file_path)
        try:
            if not os.path.exists(target_file_path_ext):
                os.makedirs(target_file_path_ext)
        except Exception as e:
            QtWidgets.QMessageBox.warning(
                self, "Fehler", f"Fehler beim Erstellen des Verzeichnisses {target_file_path.root()}.\n\n"
                f"Fehler: {e}")
        try:
            shutil.copy(source_file_path, target_file_path)
            count += 1
        except Exception as e:
            QtWidgets.QMessageBox.warning(
                self, "Fehler", f"Fehler beim Kopieren der Datei {source_file_path} zu {target_file_path}.\n\n"
                f"Fehler: {e}")
    return count


def log_and_show_result(self, source_path, target_path, source_files, matching_files, df, count, log_sub2folder_path):
    logs_and_config.log_copy_details(self, source_path, target_path,
                                     source_files, matching_files, df)

    QtWidgets.QMessageBox.information(self, "Erfolg!",
                                      f"Das Kopieren der Dateien wurde beendet.\n"
                                      f"Es wurden insgesamt {count} Dateien übertragen.\n\n"
                                      f"Es wurde eine Logdatei im log-Ordner:\n\n {log_sub2folder_path}\n\n erstellt.")

import os
import shutil
from datetime import datetime

import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QCheckBox, QMessageBox, QTableWidget, QWidget

import files.logs_and_config as logs_and_config
from directories.constants import dir_paths


def get_paths():
    source_path = dir_paths.dict["source_path"]
    target_path = dir_paths.dict["target_1_path"]
    log_sub2folder_path = dir_paths.dict["log_subfolder_2_path"]
    return source_path, target_path, log_sub2folder_path


def get_selected_files_and_df(self):
    selected_files = []
    df = pd.DataFrame(columns=["article_no", "article_name", "count"])
    table = self.ui.articles_list

    for row in range(table.rowCount()):
        cell_widget: QWidget = table.cellWidget(row, 0)

        checkbox: QCheckBox = get_child_of_type_in_table_row(
            obj=cell_widget,
            cls=QCheckBox,
        )

        article_no = table.item(row, 1).text()
        article_name = table.item(row, 2).text()

        new_data = pd.DataFrame(
            {"article_no": [article_no], "article_name": [article_name]}
        )

        df = pd.concat([df, new_data], ignore_index=True)
        if checkbox is not None and checkbox.checkState() == Qt.Checked:
            selected_files.append(article_no)

    selected_files = list(set(selected_files))
    return selected_files, df


def get_child_of_type_in_table_row(
    obj: QWidget = None,
    cls: QWidget = None,
):
    children = obj.findChildren(cls)
    child: QWidget
    for child in children:

        if isinstance(child, cls):
            return child

    return None


def get_matching_files(source_files, selected_files):
    return [
        file
        for file in source_files
        if any(selected_file in file for selected_file in selected_files)
    ]


def mark_matching_files(self, matching_files):

    table = self.ui.articles_list
    for row in range(table.rowCount()):
        article_no_item = table.item(row, 1)
        article_no = article_no_item.text()

        if any(article_no in matching_file for matching_file in matching_files):
            font = QFont()
            font.setBold(True)
            article_no_item.setFont(font)


def copy_files(self, matching_files: list, source_path: str, target_path: str) -> int:
    """
    Kopiert gewählte Dateien aus dem Quellordner nach dem Zielordner.
    Dabei wird auch die Anzahl der verschobenen Dateien gezählt, welches ausgegeben wird
    :param matching_files: Liste der gefundenen Dateien
    :param source_path: Pfad zum Quellordner
    :param target_path: Pfad zum Zielordner
        --> es werden zusätzlich zum Zielordner zwei sich verkettende Unterordner erstellt /Projektnummer/Zeitstempel
        --> weiterhin werden die Unterordner der Quelldaten beachtet und ebenfalls erstellt

    :return: Anzahl der verschobenen Dateien
    """

    count = 0

    project_no: str = self.ui.project.toPlainText()
    date: str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    for matching_filename in matching_files:
        source_file_path = os.path.join(source_path, matching_filename)
        target_file_path = os.path.join(
            target_path, project_no, date, matching_filename
        )

        try:
            # Der Pfad der Dateien, welche in Unterordnern muss vorab bestimmt werden
            target_file_path_ext = os.path.dirname(target_file_path)
            # Verzeichnis erstellen, falls es nicht existiert
            os.makedirs(target_file_path_ext, exist_ok=True)

        except Exception as e:
            QMessageBox.warning(
                self,
                "Fehler",
                f"Fehler beim Erstellen des Verzeichnisses {target_file_path.root()}.\n\n"
                f"Fehler: {e}",
            )
        try:
            shutil.copy(source_file_path, target_file_path)
            count += 1
        except Exception as e:
            QMessageBox.warning(
                self,
                "Fehler",
                f"Fehler beim Kopieren der Datei {source_file_path} zu {target_file_path}.\n\n"
                f"Fehler: {e}",
            )
    return count


def log_and_show_result(
    self,
    source_path,
    target_path,
    source_files,
    matching_files,
    df,
    count,
    log_sub2folder_path,
):
    logs_and_config.log_copy_details(
        self, source_path, target_path, source_files, matching_files, df
    )

    QMessageBox.information(
        self,
        "Erfolg!",
        f"Das Kopieren der Dateien wurde beendet.\n"
        f"Es wurden insgesamt {count} Dateien übertragen.\n\n"
        f"Es wurde eine Logdatei im log-Ordner:\n\n {log_sub2folder_path}\n\n erstellt.",
    )


def get_files_in_source_path(self, directory):
    all_files: list[str] = []

    try:
        for root, _, files in os.walk(directory):
            for file in files:
                try:
                    file_path = os.path.relpath(os.path.join(root, file), directory)
                    all_files.append(file_path)

                except Exception as e:
                    QMessageBox.warning(
                        self,
                        "Fehler!",
                        f"Die Datei für {file_path} konnte nicht gelesen werden.\n\n {e}",
                    )

        return all_files

    except Exception as e:
        QMessageBox.warning(
            self,
            "Fehler!",
            f"Die Datei für {directory} konnte nicht gelesen werden.\n\n {e}",
        )


def compare_src_docs_with_article_list(
    table: QTableWidget, row: int, all_files: list
) -> bool:
    """
    Überprüft, ob eine Artikelnummer in einer Liste von Dateinamen enthalten ist.

    Args:
        table (QtWidgets.QTableWidget): Die Tabelle, in der sich die Artikelnummer befindet.
        row (int): Die Zeile, in der sich die Artikelnummer befindet.
        all_files (list): Liste der Dateinamen, in denen gesucht wird.

    Returns:
        bool: True, wenn die Artikelnummer in einem der Dateinamen gefunden wurde, sonst False.
    """
    # Sicherstellen, dass die Artikelnummer-Zelle existiert
    article_no_item = table.item(row, 1)
    if article_no_item is None:
        return False

    article_no = article_no_item.text()

    # Überprüfen, ob die Artikelnummer in einem der Dateinamen enthalten ist
    if any(article_no in file_name for file_name in all_files):
        return True
    else:
        return False

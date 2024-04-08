import sys
import os
import shutil

import pandas as pd

from qtpy import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from ui.mainwindow import Ui_MainWindow
import directory_Handler
import ui_fields_Handler
import logs_and_config
import data_Handler
import table_search


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,
                 parent=None):
        super().__init__(parent)

        # Erstelle eine Instanz der Benutzeroberfläche aus der generierten Ui-Datei
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("SUN-DOC")
        # Variablen df und sql_query als Instanzvariable initialisieren
        self.initialize()
        # Verbinde die Signale mit den entsprechenden Slots
        self.map_ui_buttons()

    def initialize(self):
        self.project = self.ui.project.toPlainText()
        table_search.set_all_table_headers(self)
        self.previous_project_text = self.project
        logs_and_config.create_device_related_storage_list(
            self, storage_file='blacklist_path')
        logs_and_config.create_device_related_storage_list(
            self, storage_file='device_specs_list_path')
        ui_fields_Handler.config_to_fields(self)

        # query_input-Box verstecken
        self.ui.query_input.hide()
        self.ui.query_2_input.hide()

    def map_ui_buttons(self):

        #  *********************************** Mapping buttons for "Article Fetcher"-module *****************************************

        self.ui.load_articles_file_btn.clicked.connect(
            self.on_load_articles_from_file_btn_click)
        self.ui.load_articles_db_btn.clicked.connect(
            self.on_load_articles_from_db_btn_click)
        self.ui.source_path_btn.clicked.connect(
            self.on_source_path_btn_click)
        self.ui.target_path_btn.clicked.connect(
            self.on_target_path_btn_click)
        self.ui.paste_docs_btn.clicked.connect(
            self.on_copy_files_btn_click)
        self.ui.sql_query_btn.clicked.connect(
            self.on_sql_query_btn_click)

        self.ui.project.textChanged.connect(self.on_project_text_changed)

        #  *********************************** Mapping buttons for "Documentation"- module *****************************************
        self.ui.save_btn.clicked.connect(
            self.on_save_btn_click)
        self.ui.load_btn.clicked.connect(
            self.on_load_btn_click)
        self.ui.load_data_to_device_lists.clicked.connect(
            self.on_load_data_to_device_list_click)
        self.ui.load_docu_db_data_btn.clicked.connect(
            self.on_load_docu_data_from_db_btn_click)

        self.ui.move_none_PV_modules_to_blacklist.clicked.connect(
            self.on_move_none_PV_modules_to_blacklist_click)
        self.ui.move_none_PV_inverters_to_blacklist.clicked.connect(
            self.on_move_none_PV_inverters_to_blacklist_click)
        self.ui.move_none_BAT_inverters_to_blacklist.clicked.connect(
            self.on_move_none_BAT_inverters_to_blacklist_click)
        self.ui.move_none_BAT_storage_to_blacklist.clicked.connect(
            self.on_move_none_BAT_storage_to_blacklist_click)
        self.ui.move_none_CHG_point_to_blacklist.clicked.connect(
            self.on_move_none_CHG_point_to_blacklist_click)

        self.ui.sql_query_2_btn.clicked.connect(
            self.on_sql_query_2_btn_click)
        self.ui.source_btn_matstr.clicked.connect(
            self.on_source_btn_matstr_click)
        self.ui.source_btn_docu.clicked.connect(
            self.on_source_btn_docu_click)
        self.ui.target_path_btn_2.clicked.connect(
            self.on_target_path_btn_2_click)
        self.ui.create_docs_btn.clicked.connect(
            self.on_btn_create_docs_clicked)

    def on_load_articles_from_file_btn_click(self):
        # Öffne einen Dateiauswahldialog für Benutzer
        file_dialog = QFileDialog()
        file_dialog.setNameFilter(
            "CSV Files (*.csv);;Excel Files (*.xlsx);;Libre Calc Files (*.ods)")

        # Überprüfen Sie, ob der Benutzer "OK" gedrückt hat
        if file_dialog.exec_() == QFileDialog.Accepted:
            # Erhalte den ausgewählten Dateipfad
            file_path = file_dialog.selectedFiles()[0]

            # Führe hier den nachfolgenden Code aus, wenn "OK" gedrückt wurde
            # Überprüfen Sie zusätzlich, ob file_path nicht leer ist
            if file_path:
                # Lösche die vorhandenen Daten und fülle die Tabelle mit Daten aus der Datei
                ui_fields_Handler.clear_table(self)
                df = data_Handler.read_data_from_file(file_path)
                ui_fields_Handler.fill_article_list(self, df=df)

    def on_load_articles_from_db_btn_click(self):
        # Lese Daten aus der MySQL-Datenbank und speichere sie in der Instanzvariable df
        df = data_Handler.execute_query(self, query='sql1')
        logs_and_config.update_config_file(self, 'Abfrage', 'sql1',
                                           data_Handler.get_sql_query(self)['sql1'])
        # Lösche die vorhandenen Daten und fülle die Tabelle mit den Daten aus der Datenbank
        ui_fields_Handler.fill_article_list(self, df=df)

    def on_project_text_changed(self):
        ui_fields_Handler.char_validation(self)

    @directory_Handler.get_folder_path
    def on_source_path_btn_click(self, folder_path):
        self.ui.source_path_text.setPlainText(folder_path)
        logs_and_config.update_config_file(
            self, 'Pfade', 'source_path', folder_path)

    @directory_Handler.get_folder_path
    def on_target_path_btn_click(self, folder_path):
        self.ui.target_path_text.setPlainText(folder_path)
        logs_and_config.update_config_file(
            self, 'Pfade', 'target_path', folder_path)

    @directory_Handler.check_path_existence(modus=0)
    def on_copy_files_btn_click(self, *args, **kwargs):
        # Holen Sie sich Pfade für Quell- und Zielordner aus den Textfeldern
        source_path = directory_Handler.get_directories(self)[
            'source_path']
        target_path = directory_Handler.get_directories(self)[
            'target_path_1']
        log_sub2folder_path = directory_Handler.get_directories(self)[
            'log_sub2folder_path']

        # Holen Sie sich alle Dateinamen im source_path
        source_files = data_Handler.get_files_in_source_path(self, source_path)

        # Holen Sie sich alle ausgewählten Dateien im Table Widget
        selected_files = []
        df = pd.DataFrame(columns=['article_no', 'article_name', 'count'])
        for row in range(self.ui.articles_list.rowCount()):

            checkbox_item = self.ui.articles_list.item(row, 0)
            article_no = self.ui.articles_list.item(row, 1).text()
            article_name = self.ui.articles_list.item(row, 2).text()
            # ? count = self.ui.articles_list.item(row, 3).text()
            # Erstelle ein DataFrame mit den neuen Daten

            new_data = pd.DataFrame(
                {'article_no': [article_no],
                 'article_name': [article_name]
                 # ? ,'count': [count]
                 })

            # Füge die neuen Daten zum vorhandenen DataFrame hinzu
            df = pd.concat([df, new_data], ignore_index=True)

            # Überprüfe, ob die Checkbox in der aktuellen Zeile angehakt ist
            if checkbox_item and checkbox_item.checkState() == QtCore.Qt.Checked:

                selected_files.append(article_no)

        selected_files = list(set(selected_files))

        # Holen Sie sich alle Dateinamen im Quellordner, die den ausgewählten Dateien entsprechen
        matching_files = []
        matching_files = [file for file in source_files if
                          any(selected_file in file for selected_file in selected_files)]

        # Iteriere über alle übereinstimmenden Dateinamen
        count = 0
        for matching_filename in matching_files:
            # Konstruiere den vollständigen Pfad zur Quelldatei
            source_file_path = os.path.join(source_path, matching_filename)

            # Konstruiere den vollständigen Pfad zum Ziel
            target_file_path = os.path.join(target_path, matching_filename)
            target_file_path_ext = os.path.dirname(target_file_path)
            try:
                if not os.path.exists(target_file_path_ext):
                    os.makedirs(target_file_path_ext)

            except Exception as e:
                QtWidgets.QMessageBox.warning(
                    self, "Fehler", f"Fehler beim Erstellen des Verzeichnisses {target_file_path.root()}.\n\n"
                                    f"Fehler: {e}")

            # Kopiere die Datei
            try:
                shutil.copy(source_file_path, target_file_path)
                count += 1
            except Exception as e:
                QtWidgets.QMessageBox.warning(
                    self, "Fehler", f"Fehler beim Kopieren der Datei {source_file_path} zu {target_file_path}.\n\n"
                                    f"Fehler: {e}")

        # Rufen Sie die separate Funktion für das Logging auf
        logs_and_config.log_copy_details(self, source_path, target_path,
                                         source_files, matching_files, df)

        # Gib eine Erfolgsmeldung aus
        QtWidgets.QMessageBox.information(self, "Erfolg!",
                                          f"Das Kopieren der Dateien wurde beendet.\n"
                                          f"Es wurden insgesamt {count} Dateien übertragen.\n\n"
                                          f"Es wurde eine Logdatei im log-Ordner:\n\n {log_sub2folder_path}\n\n erstellt.")

    def on_sql_query_btn_click(self):

        if self.ui.query_input.isHidden():
            self.ui.query_input.show()
        else:
            self.ui.query_input.hide()


# * * * * * * * * * * * * * * * * * Documentation-module * * * * * * * * * * * * * * * *

    def on_save_btn_click(self):
        file_path = logs_and_config.create_save_file(self)
        ui_fields_Handler.save_fields_text(self, file_path)
        ui_fields_Handler.save_tables_content(self, file_path)

    def on_load_btn_click(self):
        file_path = directory_Handler.get_save_file_dir(self)
        if file_path != '':
            ui_fields_Handler.load_fields_text(self, file_path)
            ui_fields_Handler.load_tables_content(self, file_path)

    def on_btn_create_docs_clicked(self):
        ui_fields_Handler.replace_fields_in_doc1(self)

    def on_load_data_to_device_list_click(self):
        df = data_Handler.execute_query(self, query='sql1')
        logs_and_config.update_config_file(self, 'Abfrage', 'sql1',
                                           data_Handler.get_sql_query(self)['sql1'])
        ui_fields_Handler.fill_device_lists(self, df)

    def on_move_none_PV_modules_to_blacklist_click(self):
        ui_fields_Handler.remove_articles_from_list(
            self, list=self.ui.PV_modules_list)

    def on_move_none_PV_inverters_to_blacklist_click(self):
        ui_fields_Handler.remove_articles_from_list(
            self, list=self.ui.PV_inverters_list)

    def on_move_none_BAT_inverters_to_blacklist_click(self):
        ui_fields_Handler.remove_articles_from_list(
            self, list=self.ui.BAT_inverters_list)

    def on_move_none_BAT_storage_to_blacklist_click(self):
        ui_fields_Handler.remove_articles_from_list(
            self, list=self.ui.BAT_storage_list)

    def on_move_none_CHG_point_to_blacklist_click(self):
        ui_fields_Handler.remove_articles_from_list(
            self, list=self.ui.CHG_point_list)

    def on_load_docu_data_from_db_btn_click(self):
        ui_fields_Handler.check_specs_in_device_tables(self)

        df = data_Handler.execute_query(self, query='sql2')
        logs_and_config.update_config_file(self, 'Abfrage', 'sql2',
                                           data_Handler.get_sql_query(self)['sql2'])
        ui_fields_Handler.clear_docu_fields(self)
        ui_fields_Handler.fill_docu_fields(self)

    def on_sql_query_2_btn_click(self):
        if self.ui.query_2_input.isHidden():
            self.ui.query_2_input.show()
        else:
            self.ui.query_2_input.hide()

    @directory_Handler.get_file_path
    def on_source_btn_matstr_click(self, file_path):
        self.ui.source_path_text_matstr.setPlainText(file_path)
        logs_and_config.update_config_file(
            self, 'Pfade', 'template1_path', file_path)

    @directory_Handler.get_file_path
    def on_source_btn_docu_click(self, file_path):
        self.ui.source_path_text_docu.setPlainText(file_path)
        logs_and_config.update_config_file(
            self, 'Pfade', 'template2_path', file_path)

    @directory_Handler.get_folder_path
    def on_target_path_btn_2_click(self, folder_path):
        self.ui.target_path_text_2.setPlainText(folder_path)
        logs_and_config.update_config_file(
            self, 'Pfade', 'target_path_2', folder_path)


# Führe das Programm aus, wenn es direkt gestartet wird
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

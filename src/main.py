import sys

from qtpy import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from ui.mainwindow import Ui_MainWindow

import data_sources.data_base
import tables.customize_row
import tables.search_bar
import tables.tables_base
import directories.directory_base as directory_base
import files.logs_and_config as logs_and_config
import save_file
import ui_fields.ui_fields_base
from styles.styles_Handler import init_ui
import files.copy_files as copy_files

from menus import menus_base


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

        directory_base.set_static_directories()
        menus_base.initialize_all_menus(self)
        init_ui(self)

        logs_and_config.create_config_file()
        logs_and_config.create_device_related_storage_list(
            storage_file='blacklist_path')
        logs_and_config.create_device_related_storage_list(
            storage_file='device_specs_list_path')

        ui_fields.ui_fields_base.config_to_fields(self)

        tables.tables_base.connect_table_buttons(self)

        self.previous_project_text = self.ui.project.toPlainText()

    def map_ui_buttons(self):

        #  *********************************** Mapping buttons for "Article Fetcher"-module *****************************************

        self.ui.load_articles_file_btn.clicked.connect(
            self.on_load_articles_from_file_btn_click)
        self.ui.load_articles_db_btn.clicked.connect(
            self.on_load_articles_from_db_btn_click)
        self.ui.target_path_btn.clicked.connect(
            self.on_target_path_btn_click)
        self.ui.paste_docs_btn.clicked.connect(
            self.on_copy_files_btn_click)

        self.ui.project.textChanged.connect(self.on_project_text_changed)

        tables.tables_base.connect_sort_indicator_changed(self)

        #  *********************************** Settings- module *****************************************
        menus_base.map_menu_buttons(self)

        #  *********************************** Mapping buttons for "Documentation"- module *****************************************
        self.ui.load_data_to_device_lists_btn.clicked.connect(
            self.on_load_data_to_device_list_btn_click)
        self.ui.fill_fields_btn.clicked.connect(
            self.on_fill_fields_btn_click)
        self.ui.store_device_specs_btn.clicked.connect(
            self.on_store_device_specs_btn_click)

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

        self.ui.target_path_btn_2.clicked.connect(
            self.on_target_path_btn_2_click)
        self.ui.create_doc1_btn.clicked.connect(
            self.on_btn_create_doc1_clicked)
        self.ui.create_doc2_btn.clicked.connect(
            self.on_btn_create_doc2_clicked)

# * * * * * * * * * * * * * * * * * Fetcher-module * * * * * * * * * * * * * * * *

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
                df = data_sources.data_base.read_data_from_file(file_path)
                tables.tables_base.fill_article_table(
                    table=self.ui.articles_list, df=df)

    def on_load_articles_from_db_btn_click(self):
        # Lese Daten aus der MySQL-Datenbank und speichere sie in der Instanzvariable df
        df = data_sources.data_base.execute_query(self, query='sql1')
        logs_and_config.update_config_file('Abfrage', 'sql1',
                                           data_sources.data_base.get_sql_query(self)['sql1'])
        # Lösche die vorhandenen Daten und fülle die Tabelle mit den Daten aus der Datenbank
        tables.tables_base.fill_article_table(
            self, table=self.ui.articles_list, df=df)

    def on_project_text_changed(self):
        ui_fields.ui_fields_base.char_validation(self)

    @ directory_base.get_folder_path
    def on_target_path_btn_click(self, folder_path):
        self.ui.target_path_text.setPlainText(folder_path)
        directory_base.set_target_1_dir(folder_path)
        logs_and_config.update_config_file(
            'Pfade', 'target_1_path', folder_path)

    @ directory_base.check_path_existence(modus=0)
    def on_copy_files_btn_click(self, *args, **kwargs):
        source_path, target_path, log_subfolder_2_path = copy_files.get_paths()
        source_files = data_sources.data_base.get_files_in_source_path(
            self, source_path)
        selected_files, df = copy_files.get_selected_files_and_df(
            self)
        matching_files = copy_files.get_matching_files(
            source_files, selected_files)
        copy_files.mark_matching_files(self, matching_files)
        count = copy_files.copy_files(self,
                                      matching_files, source_path, target_path)

        copy_files.log_and_show_result(self,
                                       source_path, target_path, source_files, matching_files, df, count, log_subfolder_2_path)


# * * * * * * * * * * * * * * * * * Documentation-module * * * * * * * * * * * * * * * *

    def on_btn_create_doc1_clicked(self):
        directory_base.set_doc_1_dir(self)
        ui_fields.ui_fields_base.replace_fields_in_doc(
            self, doc_path='doc_1_path', template_path='template_1_path')

    def on_btn_create_doc2_clicked(self):
        _, doc_2 = directory_base.get_docs_paths(
            self.ui.project.toPlainText())
        directory_base.MAIN_PATHS.dict['doc_2_path'] = doc_2
        ui_fields.ui_fields_base.replace_fields_in_doc(
            self, doc_path='doc_2_path', template_path='template_2_path')

    def on_load_data_to_device_list_btn_click(self):
        ui_fields.ui_fields_base.clear_docu_fields(self)
        df = data_sources.data_base.execute_query(self, query='sql1')
        logs_and_config.update_config_file('Abfrage', 'sql1',
                                           data_sources.data_base.get_sql_query(self)['sql1'])
        tables.tables_base.fill_device_lists(self, df)

    def on_move_none_PV_modules_to_blacklist_click(self):
        tables.tables_base.remove_articles_from_table(
            self, table=self.ui.PV_modules_list)

    def on_move_none_PV_inverters_to_blacklist_click(self):
        tables.tables_base.remove_articles_from_table(
            self, table=self.ui.PV_inverters_list)

    def on_move_none_BAT_inverters_to_blacklist_click(self):
        tables.tables_base.remove_articles_from_table(
            self, table=self.ui.BAT_inverters_list)

    def on_move_none_BAT_storage_to_blacklist_click(self):
        tables.tables_base.remove_articles_from_table(
            self, table=self.ui.BAT_storage_list)

    def on_move_none_CHG_point_to_blacklist_click(self):
        tables.tables_base.remove_articles_from_table(
            self, table=self.ui.CHG_point_list)

    def on_fill_fields_btn_click(self):

        df = data_sources.data_base.execute_query(self, query='sql2')
        logs_and_config.update_config_file('Abfrage', 'sql2',
                                           data_sources.data_base.get_sql_query(self)['sql2'])
        ui_fields.ui_fields_base.clear_docu_fields(self)
        ui_fields.ui_fields_base.fill_docu_fields(self)

    def on_store_device_specs_btn_click(self):
        tables.tables_base.check_specs_in_device_tables(self)

    @ directory_base.get_folder_path
    def on_target_path_btn_2_click(self, folder_path):
        self.ui.target_path_text_2.setPlainText(folder_path)
        directory_base.set_target_2_dir(folder_path)
        logs_and_config.update_config_file(
            'Pfade', 'target_2_path', folder_path)

# * * * * * * * * * * * * * * * * * Settings * * * * * * * * * * * * * * * *

    def on_save_btn_click(self):
        file_path = logs_and_config.create_save_file(self)
        if file_path != '':
            save_file.save.save_fields_text(self, file_path)
            save_file.save.save_tables_content(self, file_path)

    def on_load_btn_click(self):
        file_path = directory_base.get_save_file_dir(self)
        if file_path != '':
            save_file.load.load_fields_text(self, file_path)
            save_file.load.load_tables_content(self, file_path)


# Führe das Programm aus, wenn es direkt gestartet wird
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

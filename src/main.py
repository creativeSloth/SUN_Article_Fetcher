import sys

from PyQt5.QtWidgets import QFileDialog
from qtpy import QtWidgets

from data_sources.data_base import execute_query, get_sql_query, read_data_from_file
from directories.directory_base import (
    check_path_existence,
    dir_paths,
    get_docs_paths,
    get_save_file_dir,
    set_doc_1_dir,
    set_static_directories,
    set_target_1_dir,
    set_target_2_dir,
)
from directories.dirs_decorators import get_folder_path
from files.blacklist import initialize_blacklist_dialogs
from files.file_sys_handler import (
    copy_files,
    get_files_in_source_path,
    get_matching_files,
    get_paths,
    get_selected_files_and_df,
    log_and_show_result,
    mark_matching_files,
)
from files.logs_and_config import (
    create_config_file,
    create_device_related_storage_list,
    create_save_file,
    update_config_file,
)
from save_file.load import load_fields_text, load_tables_content
from save_file.save import save_fields_text, save_tables_content
from styles.styles_Handler import initialize_ui_style
from ui.buttons.button_lists import initialize_push_buttons
from ui.buttons.custom_button import customize_push_buttons, eventFilter
from ui.fields.ui_fields_base import (
    char_validation,
    clear_docu_fields,
    config_to_fields,
    fill_docu_fields,
    replace_fields_in_doc,
)
from ui.menus import menus_base
from ui.tables.table_decorators import connect_sort_indicator_changed
from ui.tables.tables_base import (
    check_specs_in_device_tables,
    fill_article_table,
    fill_device_lists,
    initialize_table_search,
)
from ui.windows.mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Erstelle eine Instanz der Benutzeroberfläche aus der generierten Ui-Datei
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("SUN-DOC")
        # Variablen df und sql_query als Instanzvariable initialisieren
        self.initialize()
        # Verbinde die Signale mit den entsprechenden Slots
        self.map_ui_buttons()

    def initialize(self: Ui_MainWindow) -> None:

        set_static_directories()
        menus_base.initialize_menu_dialogs(self)
        initialize_blacklist_dialogs(self)
        initialize_push_buttons(self)
        initialize_table_search(self)
        customize_push_buttons(self)

        create_config_file()
        create_device_related_storage_list(storage_file="blacklist_path")
        create_device_related_storage_list(storage_file="device_specs_list_path")

        config_to_fields(self)

        initialize_ui_style(self)

        self.previous_project_text = self.ui.project.toPlainText()

    def eventFilter(self, source, event):
        return eventFilter(self, source, event)

    def map_ui_buttons(self) -> None:
        #  *********************************** Mapping buttons for "Article Fetcher"-module *****************************************

        self.ui.load_articles_file_btn.clicked.connect(
            self.on_load_articles_from_file_btn_click
        )
        self.ui.load_articles_db_btn.clicked.connect(
            self.on_load_articles_from_db_btn_click
        )
        self.ui.target_path_btn.clicked.connect(self.on_target_path_btn_click)
        self.ui.paste_docs_btn.clicked.connect(self.on_copy_files_btn_click)

        self.ui.project.textChanged.connect(self.on_project_text_changed)

        connect_sort_indicator_changed(self)

        #  *********************************** Settings- module *****************************************
        menus_base.map_menu_buttons(self)

        #  *********************************** Mapping buttons for "Documentation"- module *****************************************
        self.ui.load_data_to_device_lists_btn.clicked.connect(
            self.on_load_data_to_device_list_btn_click
        )
        self.ui.fill_fields_btn.clicked.connect(self.on_fill_fields_btn_click)
        self.ui.store_device_specs_btn.clicked.connect(
            self.on_store_device_specs_btn_click
        )

        self.ui.target_path_btn_2.clicked.connect(self.on_target_path_btn_2_click)
        self.ui.create_doc1_btn.clicked.connect(self.on_btn_create_doc1_clicked)
        self.ui.create_doc2_btn.clicked.connect(self.on_btn_create_doc2_clicked)

    # * * * * * * * * * * * * * * * * * Fetcher-module * * * * * * * * * * * * * * * *

    def on_load_articles_from_file_btn_click(self):
        # Öffne einen Dateiauswahldialog für Benutzer
        file_dialog = QFileDialog()
        file_dialog.setNameFilter(
            "CSV Files (*.csv);;Excel Files (*.xlsx);;Libre Calc Files (*.ods)"
        )

        # Überprüfen Sie, ob der Benutzer "OK" gedrückt hat
        if file_dialog.exec_() == QFileDialog.Accepted:
            # Erhalte den ausgewählten Dateipfad
            file_path = file_dialog.selectedFiles()[0]

            # Führe hier den nachfolgenden Code aus, wenn "OK" gedrückt wurde
            # Überprüfen Sie zusätzlich, ob file_path nicht leer ist
            if file_path:
                # Lösche die vorhandenen Daten und fülle die Tabelle mit Daten aus der Datei
                df = read_data_from_file(file_path)
                fill_article_table(self, table=self.ui.articles_list, df=df)

    def on_load_articles_from_db_btn_click(self):
        # Lese Daten aus der MySQL-Datenbank und speichere sie in der Instanzvariable df
        df = execute_query(self, query="sql1")
        update_config_file("Abfrage", "sql1", get_sql_query(self)["sql1"])
        # Lösche die vorhandenen Daten und fülle die Tabelle mit den Daten aus der Datenbank
        fill_article_table(self, table=self.ui.articles_list, df=df)

    def on_project_text_changed(self):
        char_validation(self)

    @get_folder_path
    def on_target_path_btn_click(self, folder_path):
        self.ui.target_path_text.setPlainText(folder_path)
        set_target_1_dir(folder_path)
        update_config_file("Pfade", "target_1_path", folder_path)

    @check_path_existence(modus=0)
    def on_copy_files_btn_click(self, *args, **kwargs):
        source_path, target_path, log_subfolder_2_path = get_paths()
        source_files = get_files_in_source_path(self, source_path)
        selected_files, df = get_selected_files_and_df(self)
        matching_files = get_matching_files(source_files, selected_files)
        mark_matching_files(self, matching_files)
        count = copy_files(self, matching_files, source_path, target_path)

        log_and_show_result(
            self,
            source_path,
            target_path,
            source_files,
            matching_files,
            df,
            count,
            log_subfolder_2_path,
        )

    # * * * * * * * * * * * * * * * * * Documentation-module * * * * * * * * * * * * * * * *

    def on_btn_create_doc1_clicked(self):
        set_doc_1_dir(self)
        replace_fields_in_doc(
            self, doc_path="doc_1_path", template_path="template_1_path"
        )

    def on_btn_create_doc2_clicked(self):
        _, doc_2 = get_docs_paths(self.ui.project.toPlainText())
        dir_paths.dict["doc_2_path"] = doc_2
        replace_fields_in_doc(
            self, doc_path="doc_2_path", template_path="template_2_path"
        )

    def on_load_data_to_device_list_btn_click(self):
        clear_docu_fields(self)
        df = execute_query(self, query="sql1")
        update_config_file("Abfrage", "sql1", get_sql_query(self)["sql1"])
        fill_device_lists(self, df)

    def on_fill_fields_btn_click(self):

        df = execute_query(self, query="sql2")
        update_config_file("Abfrage", "sql2", get_sql_query(self)["sql2"])
        clear_docu_fields(self)
        fill_docu_fields(self)

    def on_store_device_specs_btn_click(self):
        check_specs_in_device_tables(self)

    @get_folder_path
    def on_target_path_btn_2_click(self, folder_path):
        self.ui.target_path_text_2.setPlainText(folder_path)
        set_target_2_dir(folder_path)
        update_config_file("Pfade", "target_2_path", folder_path)

    # * * * * * * * * * * * * * * * * * Settings * * * * * * * * * * * * * * * *

    def on_save_btn_click(self):
        file_path = create_save_file(self)
        if file_path != "":
            save_fields_text(self, file_path)
            save_tables_content(self, file_path)

    def on_load_btn_click(self):
        file_path = get_save_file_dir(self)
        if file_path != "":
            load_fields_text(self, file_path)
            load_tables_content(self, file_path)


# Führe das Programm aus, wenn es direkt gestartet wird
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

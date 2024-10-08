from PyQt5.QtWidgets import QDialog

import directories.document_helpers
import files.logs_and_config as logs_and_config
from directories.dirs_decorators import get_file_path, get_folder_path
from styles.styles_Handler import initialize_ui_style
from ui.windows import settingsConnectionWindow, settingsPathsWindow


class SettConDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = settingsConnectionWindow.Ui_Dialog()
        self.ui.setupUi(self)
        # Variablen df und sql_query als Instanzvariable initialisieren
        self.initialize()
        # Verbinde die Signale mit den entsprechenden Slots
        self.map_ui_buttons()

    def initialize(self):
        initialize_ui_style(self)
        # query_input-Box verstecken
        self.ui.query_input.hide()
        self.ui.query_2_input.hide()

    def map_ui_buttons(self):
        self.ui.sql_query_btn.clicked.connect(self.on_sql_query_btn_click)

        self.ui.sql_query_2_btn.clicked.connect(self.on_sql_query_2_btn_click)

    def on_sql_query_btn_click(self):
        if self.ui.query_input.isHidden():
            self.ui.query_input.show()
        else:
            self.ui.query_input.hide()

    def on_sql_query_2_btn_click(self):
        if self.ui.query_2_input.isHidden():
            self.ui.query_2_input.show()
        else:
            self.ui.query_2_input.hide()


class SettPathsDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = settingsPathsWindow.Ui_Dialog()
        self.ui.setupUi(self)
        # Variablen df und sql_query als Instanzvariable initialisieren
        self.initialize()
        # Verbinde die Signale mit den entsprechenden Slots
        self.map_ui_buttons()

    def initialize(self):
        initialize_ui_style(self)

    def map_ui_buttons(self):
        self.ui.source_path_btn.clicked.connect(self.on_source_path_btn_click)
        self.ui.source_btn_matstr.clicked.connect(self.on_source_btn_matstr_click)
        self.ui.source_btn_docu.clicked.connect(self.on_source_btn_docu_click)

    @get_folder_path
    def on_source_path_btn_click(self, folder_path):
        self.ui.source_path_text.setPlainText(folder_path)
        directories.document_helpers.set_source_dir(dir=folder_path)
        logs_and_config.update_config_file("Pfade", "source_path", folder_path)

    @get_file_path
    def on_source_btn_matstr_click(self, file_path):
        self.ui.source_path_text_matstr.setPlainText(file_path)
        directories.document_helpers.set_template_dir(
            template="template_1_path", dir=file_path
        )
        logs_and_config.update_config_file("Pfade", "template_1_path", file_path)

    @get_file_path
    def on_source_btn_docu_click(self, file_path):
        self.ui.source_path_text_docu.setPlainText(file_path)
        directories.document_helpers.set_template_dir(
            template="template_2_path", dir=file_path
        )
        logs_and_config.update_config_file("Pfade", "template_2_path", file_path)

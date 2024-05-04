from qtpy import QtWidgets

from ui import settingsConnectionWindow


class SettConDlg(QtWidgets.QDialog):
    def __init__(self,
                 parent=None):
        super().__init__(parent)
        self.ui = settingsConnectionWindow.Ui_Dialog()
        self.ui.setupUi(self)
        # Variablen df und sql_query als Instanzvariable initialisieren
        self.initialize()
        # Verbinde die Signale mit den entsprechenden Slots
        self.map_ui_buttons()

    def initialize(self):
        # query_input-Box verstecken
        self.ui.query_input.hide()
        self.ui.query_2_input.hide()

    def map_ui_buttons(self):
        self.ui.sql_query_btn.clicked.connect(
            self.on_sql_query_btn_click)

        self.ui.sql_query_2_btn.clicked.connect(
            self.on_sql_query_2_btn_click)

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

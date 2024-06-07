from menus.menu_settings import SettConDlg, SettPathsDlg


def initialize_menu_dialogs(self):
    self.sett_con_dlg = SettConDlg()
    self.sett_paths_dlg = SettPathsDlg()


def show_menu(*args):
    args[0].show()


def map_menu_buttons(self):
    self.ui.actionConnection.triggered.connect(lambda: show_menu(self.sett_con_dlg))
    self.ui.actionPaths.triggered.connect(lambda: show_menu(self.sett_paths_dlg))

    self.ui.actionSave.triggered.connect(self.on_save_btn_click)
    self.ui.actionLoad.triggered.connect(self.on_load_btn_click)

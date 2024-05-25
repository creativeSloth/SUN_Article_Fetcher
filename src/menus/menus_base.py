import menus.menu_settings as menu_settings


def initialize_menu_dialogs(self):
    self.sett_con_dlg = menu_settings.SettConDlg()
    self.sett_paths_dlg = menu_settings.SettPathsDlg()


def show_menu(*args):
    args[0].show()


def map_menu_buttons(self):
    self.ui.actionConnection.triggered.connect(
        lambda: show_menu(self.sett_con_dlg))
    self.ui.actionPaths.triggered.connect(
        lambda: show_menu(self.sett_paths_dlg))

    self.ui.actionSave.triggered.connect(self.on_save_btn_click)
    self.ui.actionLoad.triggered.connect(self.on_load_btn_click)

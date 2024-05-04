import menus.sett_con as sett_con


def initialize_all_menus(self):
    self.ui_sett_con_dlg = sett_con.SettConDlg()


def show_menu(*args):
    args[0].show()


def map_menu_buttons(self):
    self.ui.actionConnection.triggered.connect(
        lambda: show_menu(self.ui_sett_con_dlg))
    self.ui.actionSave.triggered.connect(self.on_save_btn_click)
    self.ui.actionLoad.triggered.connect(self.on_load_btn_click)

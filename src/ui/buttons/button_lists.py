from PyQt5.QtWidgets import QMainWindow, QPushButton


class ButtonLists:
    def __init__(self):
        self._search_btns: list[QPushButton] = []
        self._move_BL_btns: list[QPushButton] = []
        self._doc_avlble_btns: list[QPushButton] = []

    def add_generic_button(self, button: QPushButton, button_type: str) -> None:

        if button_type == "search":
            self._search_btns.append(button)
        elif button_type == "doc_available":
            self._doc_avlble_btns.append(button)

    def add_move_bl_button(self, window: QMainWindow) -> None:

        self._move_BL_btns = [
            window.ui.move_none_PV_modules_to_blacklist,
            window.ui.move_none_PV_inverters_to_blacklist,
            window.ui.move_none_BAT_inverters_to_blacklist,
            window.ui.move_none_BAT_storage_to_blacklist,
            window.ui.move_none_CHG_point_to_blacklist,
        ]

    def get_search_buttons(self):
        return self._search_btns

    def get_move_bl_buttons(self):
        return self._move_BL_btns

    def get_doc_available_buttons(self):
        return self._doc_avlble_btns

    def reset_list(self, list_attr: str = None):
        if list_attr == "search":
            self._search_btns = []
        elif list_attr == "move_bl":
            self._move_BL_btns = []
        elif list_attr == "doc_available":
            self._doc_avlble_btns = []


def initialize_push_buttons(self):
    # Erstelle eine PushButton-Instanz
    self.button_list = ButtonLists()
    self.button_list.add_move_bl_button(window=self)

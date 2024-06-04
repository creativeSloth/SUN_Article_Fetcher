from PyQt5.QtWidgets import QPushButton


class ButtonLists:
    def __init__(self):
        self._SEARCH_BTN_LIST: list[QPushButton] = []
        self._MOVE_BL_BTN_LIST: list[QPushButton] = []

    def add_search_button(self, button: QPushButton) -> None:
        self._SEARCH_BTN_LIST.append(button)

    def add_move_bl_button(self, window) -> None:
        self._MOVE_BL_BTN_LIST = [
            window.ui.move_none_PV_modules_to_blacklist,
            window.ui.move_none_PV_inverters_to_blacklist,
            window.ui.move_none_BAT_inverters_to_blacklist,
            window.ui.move_none_BAT_storage_to_blacklist,
            window.ui.move_none_CHG_point_to_blacklist,
        ]

    def get_search_buttons(self):
        return self._SEARCH_BTN_LIST

    def get_move_bl_buttons(self):
        return self._MOVE_BL_BTN_LIST


def initialize_push_buttons(self):
    # Erstelle eine PushButton-Instanz
    self.button_list = ButtonLists()
    self.button_list.add_move_bl_button(window=self)

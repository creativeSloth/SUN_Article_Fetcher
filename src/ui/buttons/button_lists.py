from PyQt5.QtWidgets import QPushButton


class ButtonLists:
    def __init__(self):
        self.SEARCH_BTN_LIST: list[QPushButton] = []
        self.MOVE_BL_BTN_LIST: list[QPushButton] = []

    def add_button(self, button: QPushButton, list: list) -> None:
        list.append(button)


def initialize_push_buttons(self):
    # Erstelle eine PushButton-Instanz
    self.button_list = ButtonLists()

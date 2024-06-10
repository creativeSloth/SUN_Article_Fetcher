from PyQt5.QtWidgets import QMainWindow, QPushButton

from files.file_sys_handler import compare_src_docs_with_article_list
from ui.buttons.custom_button import create_button_into_table_cell


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


def add_doc_avlbl_btns(self, table, all_files):
    self.button_list: ButtonLists
    self.button_list.reset_list(list_attr="doc_available")
    for row in range(table.rowCount()):
        has_doc = compare_src_docs_with_article_list(table, row, all_files)
        if has_doc:
            push_button = create_button_into_table_cell(
                self,
                table_of_cell=table,
                row=row,
                column=0,
                text="",
                on_button_pressed=None,
            )

            self.button_list.add_generic_button(
                button=push_button, button_type="doc_available"
            )

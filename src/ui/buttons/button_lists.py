from PyQt5.QtWidgets import QMainWindow, QPushButton, QTableWidget

from files.file_sys_handler import compare_src_docs_with_article_list
from ui.buttons.custom_button import create_button_into_table_cell


class ButtonLists:
    def __init__(self):
        self._search_btns: list[QPushButton] = []
        self._move_BL_btns: list[QPushButton] = []
        self._doc_avlble_btns: list[QPushButton] = []
        self._move_to_article_list_bl_btns: list[QPushButton] = []

    def add_generic_button(self, button: QPushButton, button_type: str) -> None:

        if button_type == "search":
            self._search_btns.append(button)
        elif button_type == "doc_available":
            self._doc_avlble_btns.append(button)
        elif button_type == "move_to_blacklist":
            self._move_to_article_list_bl_btns.append(button)

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

    def get_move_to_article_list_bl_buttons(self):
        return self._move_to_article_list_bl_btns

    def reset_list(self, list_attr: str = None):
        if list_attr == "search":
            self._search_btns = []
        elif list_attr == "move_bl":
            self._move_BL_btns = []
        elif list_attr == "doc_available":
            self._doc_avlble_btns = []
        elif list_attr == "move_to_article_list_bl":
            self._move_to_article_list_bl_btns = []


def initialize_push_buttons(self):
    self.ui.load_articles_file_btn.hide()
    # Erstelle eine PushButton-Instanz
    self.button_list = ButtonLists()
    self.button_list.add_move_bl_button(window=self)


def add_doc_avlbl_btns(
    self, table: QTableWidget, all_files: list = [str], on_button_pressed=None
) -> None:
    self.button_list.reset_list(list_attr="doc_available")
    for row in range(table.rowCount()):
        has_doc = compare_src_docs_with_article_list(table, row, all_files)
        if has_doc:
            add_pushbutton(
                self,
                table=table,
                row=row,
                column=0,
                button_type="doc_available",
                on_button_pressed=on_button_pressed,
            )


def add_move_to_article_list_bl_btns(self, table: QTableWidget) -> None:
    from ui.tables.tables_base import remove_article_from_table_row

    self.button_list.reset_list(list_attr="move_to_article_list_bl")
    for row in range(table.rowCount()):
        add_pushbutton(
            self,
            table=table,
            row=row,
            column=4,
            button_type="move_to_article_list_bl",
            on_button_pressed=remove_article_from_table_row,
        )


def create_remove_from_bl_btn(self, table_of_cell: QTableWidget) -> None:
    from files.blacklist import on_remove_articles_from_ui_bl

    row_count = table_of_cell.rowCount()
    for row in range(row_count):
        create_button_into_table_cell(
            self,
            table_of_cell=table_of_cell,
            row=row,
            column=3,
            text="[X]",
            on_button_pressed=on_remove_articles_from_ui_bl,
        )


def add_pushbutton(
    self,
    table: QTableWidget,
    row: int,
    column: int,
    button_type: str,
    on_button_pressed: None,
):
    push_button = create_button_into_table_cell(
        self,
        table_of_cell=table,
        row=row,
        column=column,
        text="",
        on_button_pressed=on_button_pressed,
    )

    self.button_list.add_generic_button(button=push_button, button_type=button_type)

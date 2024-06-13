from ast import If

from PyQt5.QtWidgets import QMainWindow, QPushButton, QTableWidget

from files.file_sys_handler import compare_src_docs_with_article_list
from ui.buttons.custom_button import create_button_into_table_cell


class ButtonLists:
    def __init__(self):
        self._search_btns: list[QPushButton] = []
        self._doc_avlble_btns: list[QPushButton] = []
        self._move_to_BL_btns = {
            "articles_list": [],
            "PV_modules_list": [],
            "PV_inverters_list": [],
            "BAT_inverters_list": [],
            "BAT_storage_list": [],
            "CHG_point_list": [],
        }
        self._open_BL_btns: list[QPushButton] = []
        self._move_from_BL_btns: list[QPushButton] = []

    def add_open_BL_btns(self, window):

        self._open_BL_btns = [
            window.ui.open_articles_blacklist,
            window.ui.open_PV_modules_blacklist,
            window.ui.open_PV_inverters_blacklist,
            window.ui.open_BAT_inverters_blacklist,
            window.ui.open_BAT_storage_blacklist,
            window.ui.open_CHG_point_blacklist,
        ]

    def add_generic_button(
        self,
        table_name: str = None,
        button: QPushButton = None,
        button_type: str = None,
    ) -> None:

        if button_type == "search":
            self._search_btns.append(button)
        elif button_type == "doc_available":
            self._doc_avlble_btns.append(button)
        elif button_type == "move_to_bl":
            self._move_to_BL_btns[table_name].append(button)

    def get_search_btns(self):
        return self._search_btns

    def get_move_from_bl_btns(self):
        return self._move_from_BL_btns

    def get_doc_available_btns(self):
        return self._doc_avlble_btns

    def get_open_BL_btns(self):
        return self._open_BL_btns

    def get_move_to_bl_btns(self, table_name: str = None):
        if table_name is not None:
            return self._move_to_BL_btns[table_name]

    def reset_list(self, button_type: str = None, table_name: str = None):
        if button_type == "search":
            self._search_btns = []
        elif button_type == "move_from_BL":
            self._move_from_BL_btns = []
        elif button_type == "doc_available":
            self._doc_avlble_btns = []
        elif button_type == "move_to_bl":
            self._move_to_BL_btns[table_name] = []


def initialize_push_buttons(self):
    self.ui.load_articles_file_btn.hide()
    # Erstelle eine PushButton-Instanz
    self.button_list = ButtonLists()
    self.button_list.add_open_BL_btns(window=self)


def add_doc_avlbl_btns(
    self, table: QTableWidget, all_files: list = [str], on_button_pressed=None
) -> None:
    self.button_list.reset_list(
        button_type="doc_available", table_name=table.objectName()
    )
    for row in range(table.rowCount()):
        has_doc = compare_src_docs_with_article_list(table, row, all_files)
        if has_doc:
            add_pushbutton_to_button_list(
                self,
                table=table,
                row=row,
                column=0,
                button_type="doc_available",
                on_button_pressed=on_button_pressed,
            )


def add_move_to_bl_btns(self, table: QTableWidget, column: int) -> None:
    from ui.tables.tables_base import remove_article_from_table_row

    button_type = "move_to_bl"
    self.button_list.reset_list(button_type=button_type, table_name=table.objectName())
    for row in range(table.rowCount()):
        add_pushbutton_to_button_list(
            self,
            table=table,
            row=row,
            column=column,
            button_type=button_type,
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
            text="x",
            on_button_pressed=on_remove_articles_from_ui_bl,
        )


def add_pushbutton_to_button_list(
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

    self.button_list.add_generic_button(
        table_name=table.objectName(), button=push_button, button_type=button_type
    )

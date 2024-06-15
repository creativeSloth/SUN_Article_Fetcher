from typing import Any

from PyQt5.QtWidgets import QPushButton, QTableWidget

from files.file_sys_handler import compare_src_docs_with_article_list
from ui.buttons.utils import (
    create_and_set_obj_property,
    list_objects_of_class,
    list_of_property_members,
)
from ui.fields.ui_fields_base import get_all_mainwindow_tables


class ButtonLists:
    def __init__(self, parent=None):
        self.parent = parent
        self._search_btns: list[QPushButton] = []
        self._doc_avlble_btns: list[QPushButton] = []
        self._open_BL_btns: list[QPushButton] = []
        self._move_from_BL_btns = []

        self._move_to_BL_btns: dict[str, list] = {
            "articles_list": [],
            "PV_modules_list": [],
            "PV_inverters_list": [],
            "BAT_inverters_list": [],
            "BAT_storage_list": [],
            "CHG_point_list": [],
        }

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

    def refresh(self):

        all_pushbuttons = list_objects_of_class(
            parent=self.parent,
            cls=QPushButton,
        )

        self._doc_avlble_btns = list_of_property_members(
            property_type="button_type",
            property_value="doc_available",
            wanted_objs=all_pushbuttons,
        )
        self._search_btns = list_of_property_members(
            property_type="button_type",
            property_value="search",
            wanted_objs=all_pushbuttons,
        )
        self._move_from_BL_btns = list_of_property_members(
            property_type="button_type",
            property_value="move_from_bl",
            wanted_objs=all_pushbuttons,
        )

        self._move_to_BL_btns = {}
        for table in get_all_mainwindow_tables(self.parent):
            table_name = table.objectName()
            self._move_to_BL_btns[table_name] = list_of_property_members(
                property_type="button_type",
                property_value="move_to_bl",
                wanted_objs=all_pushbuttons,
            )


def initialize_push_buttons(self):
    self.ui.load_articles_file_btn.hide()

    # Erstelle eine PushButton-Instanz
    self.button_list = ButtonLists(self)

    set_btn_attr_of_open_BL_btns(self)
    self.button_list.refresh()


def set_btn_attr_of_open_BL_btns(self):

    open_BL_btns = [
        (self.ui.open_articles_blacklist, self.ui.articles_list),
        (self.ui.open_PV_modules_blacklist, self.ui.PV_modules_list),
        (self.ui.open_PV_inverters_blacklist, self.ui.PV_inverters_list),
        (self.ui.open_BAT_inverters_blacklist, self.ui.BAT_inverters_list),
        (self.ui.open_BAT_storage_blacklist, self.ui.BAT_storage_list),
        (self.ui.open_CHG_point_blacklist, self.ui.CHG_point_list),
    ]

    # Ersetzen Sie die vorhandenen QPushButton-Instanzen durch die benutzerdefinierte Klasse
    self._open_BL_btns = [
        create_and_set_obj_property(
            obj=open_BL_btn, property_type="button_type", property_value="open_bl"
        )
        for open_BL_btn, _ in open_BL_btns
    ]


def add_doc_avlbl_btns(
    self,
    table: QTableWidget = None,
    column: int = 0,
    button_type: str = None,
    all_files: list = [str],
    on_button_pressed: Any = None,
) -> None:

    for row in range(table.rowCount()):
        has_doc = compare_src_docs_with_article_list(table, row, all_files)
        if has_doc:
            create_button_into_table_cell(
                self,
                table_of_cell=table,
                row=row,
                column=column,
                button_type=button_type,
                on_button_pressed=on_button_pressed,
            )


def add_btns_into_table_cells(
    self,
    table: QTableWidget = None,
    column: int = None,
    button_type: str = "",
    on_button_pressed: Any = None,
) -> None:

    for row in range(table.rowCount()):
        create_button_into_table_cell(
            self,
            table_of_cell=table,
            row=row,
            column=column,
            button_type=button_type,
            on_button_pressed=on_button_pressed,
        )


def create_button_into_table_cell(
    self,
    table_of_cell: QTableWidget = None,
    row: int = None,
    column: int = 0,
    button_type: str = "",
    text: str = "",
    on_button_pressed=None,
) -> None:

    # Erstelle dynamisch ein Attribut für jede Tabelle
    setattr(self, f"{table_of_cell}_{row}_push_button", QPushButton(text))
    push_button = getattr(self, f"{table_of_cell}_{row}_push_button", None)

    create_and_set_obj_property(
        obj=push_button, property_type="button_type", property_value=button_type
    )

    push_button.setFixedSize(25, 25)

    if on_button_pressed:
        push_button.clicked.connect(
            lambda _, tbl=table_of_cell, btn=push_button: on_button_pressed(tbl, btn)
        )

    table_of_cell.setCellWidget(row, column, push_button)

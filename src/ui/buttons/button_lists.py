from typing import Any, Union

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QTableWidget

from files.file_sys_handler import compare_src_docs_with_article_list
from ui.buttons.button_subclasses import (
    QPushButton_del_from_bl,
    QPushButton_del_to_bl,
    QPushButton_doc,
    QPushButton_open_bl,
    QPushButton_search,
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

        self._button_type_map: dict[str, tuple] = {
            "search": [self._search_btns, QPushButton_search],
            "doc_available": [self._doc_avlble_btns, QPushButton_doc],
            "move_from_bl": [self._move_from_BL_btns, QPushButton_del_from_bl],
            "move_to_bl": [self._move_to_BL_btns, QPushButton_del_to_bl],
            "open_bl": [self._move_to_BL_btns, QPushButton_open_bl],
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

        self._doc_avlble_btns = list_objects_of_class(self.parent, QPushButton_doc)
        self._search_btns = list_objects_of_class(self.parent, QPushButton_search)
        self._move_from_BL_btns = list_objects_of_class(
            self.parent, QPushButton_del_from_bl
        )

        self._move_to_BL_btns = {}
        for table in get_all_mainwindow_tables(self.parent):
            table_name = table.objectName()
            self._move_to_BL_btns[table_name] = list_objects_of_class(
                self.parent, QPushButton_del_to_bl
            )


def list_objects_of_class(parent, cls):
    return parent.findChildren(cls)


def initialize_push_buttons(self):
    self.ui.load_articles_file_btn.hide()

    # Erstelle eine PushButton-Instanz
    self.button_list = ButtonLists(self)

    change_class_of_open_BL_btns(self)
    self.button_list.refresh()


def change_class_of_open_BL_btns(self):

    open_BL_btns = [
        self.ui.open_articles_blacklist,
        self.ui.open_PV_modules_blacklist,
        self.ui.open_PV_inverters_blacklist,
        self.ui.open_BAT_inverters_blacklist,
        self.ui.open_BAT_storage_blacklist,
        self.ui.open_CHG_point_blacklist,
    ]
    # Ersetzen Sie die vorhandenen QPushButton-Instanzen durch die benutzerdefinierte Klasse
    self._open_BL_btns = [
        replace_with_custom_class(open_BL_btn, QPushButton_open_bl)
        for open_BL_btn in open_BL_btns
    ]


def replace_with_custom_class(original_button, custom_class):
    new_button = custom_class(original_button.text())
    new_button.setObjectName(original_button.objectName())
    new_button.setGeometry(original_button.geometry())
    new_button.setFont(original_button.font())
    new_button.setIcon(original_button.icon())
    new_button.setIconSize(original_button.iconSize())
    new_button.setEnabled(original_button.isEnabled())
    new_button.setVisible(original_button.isVisible())
    # Weitere Eigenschaften, die kopiert werden müssen, hier hinzufügen

    # Ersetzen Sie das ursprüngliche Widget in seinem Layout
    parent_frame = original_button.parentWidget()
    if parent_frame is not None:
        original_button.setParent(None)
        new_button.setParent(parent_frame)
        new_button.raise_()

    return new_button


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
        self.button_list.refresh()


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
        self.button_list.refresh()


def pick_button_class(
    self, button_type
) -> Union[
    QPushButton, QPushButton_del_from_bl, QPushButton_del_to_bl, QPushButton_doc
]:
    return self.button_list._button_type_map[button_type][1]


def create_button_into_table_cell(
    self,
    table_of_cell: QtWidgets.QTableWidget = None,
    row: int = None,
    column: int = 0,
    button_type: str = "",
    text: str = "",
    on_button_pressed=None,
) -> None:

    button_class = pick_button_class(self, button_type)

    # Erstelle dynamisch ein Attribut für jede Tabelle
    setattr(self, f"{table_of_cell}_{row}_push_button", button_class(text))
    push_button = getattr(self, f"{table_of_cell}_{row}_push_button", None)

    push_button.setFixedSize(25, 25)

    if on_button_pressed:
        push_button.clicked.connect(
            lambda _, tbl=table_of_cell, btn=push_button: on_button_pressed(tbl, btn)
        )

    table_of_cell.setCellWidget(row, column, push_button)

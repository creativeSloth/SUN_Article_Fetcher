from typing import Any

from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QTableWidget

from files.sys_files import compare_src_docs_with_article_no
from ui.buttons.custom_button import customize_dynamic_pb
from ui.buttons.utils import (
    create_and_set_obj_property,
    list_objects_of_class,
    list_of_property_members,
    set_cell_widget,
    set_pushbutton_for_cell,
)
from ui.text_edits.ui_fields_base import get_all_mainwindow_tables


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
        from ui.blacklists.constants import BLACKLISTS

        blacklist_pushbuttons: list[QPushButton] = []
        all_pushbuttons: list[QPushButton] = []
        pbs_of_hlayout: list[QPushButton] = []

        for blacklist in BLACKLISTS:
            blacklist_pushbuttons = list_objects_of_class(
                parent=blacklist,
                cls=QPushButton,
            )
            all_pushbuttons.extend(blacklist_pushbuttons)

        for h_box_layout in list_objects_of_class(parent=self.parent, cls=QHBoxLayout):
            item_count = h_box_layout.count()
            for i in range(item_count):
                child = h_box_layout.itemAt(i).widget()
                if isinstance(child, QPushButton):
                    pbs_of_hlayout.append(child)
        all_pushbuttons.extend(pbs_of_hlayout)

        all_pushbuttons.extend(
            list_objects_of_class(
                parent=self.parent,
                cls=QPushButton,
            )
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

        self._open_BL_btns = list_of_property_members(
            property_type="button_type",
            property_value="open_bl",
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
    from ui.blacklists.gui_window import init_blacklist_button_click_signal

    self.ui.load_articles_file_btn.hide()

    # Erstelle eine PushButton-Instanz
    self.button_list = ButtonLists(self)
    # Initializiere die PushButton zum öffnen der Blackliste der jeweiligen Tabelle
    init_blacklist_button_click_signal(self)

    set_btn_attr_of_open_BL_btns(self)


def set_btn_attr_of_open_BL_btns(self):

    open_BL_btns = [
        (self.ui.open_articles_blacklist),
        (self.ui.open_PV_modules_blacklist),
        (self.ui.open_PV_inverters_blacklist),
        (self.ui.open_BAT_inverters_blacklist),
        (self.ui.open_BAT_storage_blacklist),
        (self.ui.open_CHG_point_blacklist),
    ]

    # Ersetzen Sie die vorhandenen QPushButton-Instanzen durch die benutzerdefinierte Klasse
    self._open_BL_btns = [
        create_and_set_obj_property(
            obj=open_BL_btn, property_type="button_type", property_value="open_bl"
        )
        for open_BL_btn in open_BL_btns
    ]


def add_doc_avlbl_btns(
    self,
    table: QTableWidget = None,
    column: int = 0,
    button_type: str = None,
    all_files: list = [str],
    on_button_pressed: Any = None,
    row: int = 0,
) -> None:

    # for row in range(table.rowCount()):
    has_doc = compare_src_docs_with_article_no(table, row, all_files)
    if has_doc:
        add_btns_into_table_cells(
            self,
            table_of_cell=table,
            row=row,
            column=column,
            button_type=button_type,
            on_button_pressed=on_button_pressed,
        )


def add_btns_into_table_cells(
    self,
    table_of_cell: QTableWidget = None,
    row: int = 0,
    column: int = None,
    button_type: str = "",
    on_button_pressed: Any = None,
    window_instance: Any = None,
) -> None:
    if window_instance is not None:
        self = window_instance

    push_button = set_pushbutton_for_cell(
        self, table_of_cell, row, column, button_type, on_button_pressed
    )

    customize_dynamic_pb(self, push_button)

    cell_widget = set_cell_widget(table_of_cell, row, column, push_button)

    table_of_cell.setCellWidget(row, column, cell_widget)

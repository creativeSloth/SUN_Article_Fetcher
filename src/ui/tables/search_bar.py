from typing import Any

from PyQt5.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTextEdit,
    QVBoxLayout,
)

from ui.buttons.utils import create_and_set_obj_property
from ui.tables.decorators import customize_table_row


def add_table_header_search_box(self, table, layout):
    index = layout.indexOf(table)
    search_layout = QHBoxLayout()
    search_layout.setSpacing(5)
    search_layout.setContentsMargins(0, 0, 0, 5)

    min_height, max_height, min_width, max_width = 30, 30, 30, 30

    # Erstelle und füge den Such-Button hinzu
    push_button = QPushButton("")
    add_search_bar_itms_attrs(push_button, "button_type", table, on_search_button_click)
    push_button.setMinimumHeight(min_height)
    push_button.setMaximumHeight(max_height)
    push_button.setMinimumWidth(min_width)
    push_button.setMaximumWidth(max_width)
    push_button.setObjectName(table.objectName() + "_search_button")
    search_layout.addWidget(push_button)

    # Erstelle und füge das Suchfeld hinzu
    text_edit = QTextEdit()
    add_search_bar_itms_attrs(
        text_edit, "text_edit_type", table, on_search_button_click
    )

    text_edit.installEventFilter(self)

    text_edit.setMaximumHeight(max_height)
    text_edit.setObjectName(table.objectName() + "_search_text_edit")
    search_layout.addWidget(text_edit)

    # Kombiniere Suchleiste und Tabelle in einem Layout
    comb_search_layout = QVBoxLayout()
    comb_search_layout.insertLayout(0, search_layout)
    comb_search_layout.addWidget(table)
    table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    layout.insertLayout(index, comb_search_layout)
    return push_button, text_edit


def init_search_button_click_signal(self, table, button, text_edit):
    button.clicked.connect(
        lambda: on_search_button_click(self, table=table, text_edit=text_edit)
    )


@customize_table_row
def on_search_button_click(self, table: QTableWidget, text_edit: QTextEdit):
    search_string = text_edit.toPlainText()
    hide_rows_without_string(table, search_string)


def hide_rows_without_string(table: QTableWidget, search_string: str):
    search_string_lower = search_string.lower()
    for row in range(table.rowCount()):
        found = False
        for col in range(table.columnCount()):
            item = table.item(row, col)
            if item is not None and search_string_lower in item.text().lower():
                found = True
                break
        table.setRowHidden(row, not found)


def add_search_bar_itms_attrs(
    obj: Any, attr: str = "", table: QTableWidget = None, func: Any = None
) -> None:
    create_and_set_obj_property(obj, property_type=attr, property_value="search")
    if func:
        create_and_set_obj_property(obj, property_type="func", property_value=func)
    if table:
        create_and_set_obj_property(obj, property_type="table", property_value=table)

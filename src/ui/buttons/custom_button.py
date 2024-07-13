import os
from ast import Tuple
from typing import Dict

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon, QPainter, QPixmap

from directories.constants import DIRS
from ui.text_edits.ui_fields_base import get_all_mainwindow_tables


def get_paths_of_icons(icon_name: str = None):
    icon_folder_path = DIRS.paths["icons_folder_path"]

    default_color_appendix = "_48dp_WHITE.png"

    if icon_name is not None:
        button_icon_path = os.path.join(
            icon_folder_path, f"{icon_name}{default_color_appendix}"
        )

    return button_icon_path


def get_button_icons_color_connected(
    self,
) -> Dict:
    """Get the Icon-Color connected to the Pushbutton.
    Returns:
        dict[QPushButton, Tuple[dict, dict]


    """

    PB_MAP: dict = {}
    PB_MAP = {
        self.ui.load_articles_db_btn: (
            get_paths_of_icons("database"),
            get_color_combo("red"),
        ),
        self.ui.load_articles_file_btn: (
            get_paths_of_icons("home_storage"),
            get_color_combo("red"),
        ),
        self.ui.target_path_btn: (
            get_paths_of_icons("drive_folder"),
            get_color_combo("blue"),
        ),
        self.ui.paste_docs_btn: (
            get_paths_of_icons("file_copy"),
            get_color_combo("blue"),
        ),
        self.ui.create_doc1_btn: (
            get_paths_of_icons("quick_reference"),
            get_color_combo("blue"),
        ),
        self.ui.create_doc2_btn: (
            get_paths_of_icons("description"),
            get_color_combo("blue"),
        ),
        self.ui.target_path_btn_2: (
            get_paths_of_icons("drive_folder"),
            get_color_combo("blue"),
        ),
        self.ui.load_data_to_device_lists_btn: (
            get_paths_of_icons("view_list"),
            get_color_combo("red"),
        ),
        self.ui.fill_fields_btn: (
            get_paths_of_icons("variable_insert"),
            get_color_combo("red"),
        ),
        self.ui.store_device_specs_btn: (
            get_paths_of_icons("export_notes"),
            get_color_combo("red"),
        ),
    }
    for button in self.button_list.get_search_btns():
        PB_MAP[button] = (get_paths_of_icons("search"), get_color_combo("blue"))

    for button in self.button_list.get_open_BL_btns():
        PB_MAP[button] = (get_paths_of_icons("preview_off"), get_color_combo("black"))

    for button in self.button_list.get_doc_available_btns():
        PB_MAP[button] = (get_paths_of_icons("documents"), get_color_combo("gold"))

    for table in get_all_mainwindow_tables(self):
        table_name = table.objectName()
        for button in self.button_list.get_move_to_bl_btns(table_name=table_name):
            PB_MAP[button] = (
                get_paths_of_icons("list_remove"),
                get_color_combo("red"),
            )

    for button in self.button_list.get_move_from_bl_btns():
        PB_MAP[button] = (get_paths_of_icons("list_add"), get_color_combo("green"))

    return PB_MAP


def customize_push_buttons(self):
    self.button_list.refresh()

    # Setze die Icons und füge Event-Filter hinzu
    PB_MAP = get_button_icons_color_connected(self)
    colored_PB_MAP = create_colored_PB_MAP(PB_MAP)

    for button, icons in colored_PB_MAP.items():
        normal_icon_path, hover_icon_path, click_icon_path = icons
        # Standard-Icon setzen
        button.setIcon(QIcon(normal_icon_path))
        button.setIconSize(button.size())

        # Icons als Button-Attribute speichern
        button.normal_icon = QIcon(normal_icon_path)
        button.hover_icon = QIcon(hover_icon_path)
        button.click_icon = QIcon(click_icon_path)

        # Event-Filter hinzufügen
        button.installEventFilter(self)


def create_colored_PB_MAP(PB_MAP: dict):
    colored_PB_MAP: dict = {}
    for button, value in PB_MAP.items():
        icon_path, color_combo = value
        normal_icon, hover_icon, click_icon = create_icon_variaties(
            icon_path, color_combo
        )
        colored_PB_MAP[button] = (normal_icon, hover_icon, click_icon)

    return colored_PB_MAP


def get_color_combo(buttoncolor=None):
    combos = {
        "blue": {
            "normal": QColor(19, 33, 59, 255),
            "hover": QColor(19, 33, 59, 60),
            "click": QColor(19, 33, 59, 20),
        },
        "red": {
            "normal": QColor(226, 24, 57, 255),
            "hover": QColor(226, 24, 58, 61),
            "click": QColor(226, 24, 58, 20),
        },
        "yellow": {
            "normal": QColor(255, 255, 0, 255),
            "hover": QColor(255, 255, 0, 60),
            "click": QColor(255, 255, 0, 20),
        },
        "green": {
            "normal": QColor(0, 255, 0, 255),
            "hover": QColor(0, 255, 0, 60),
            "click": QColor(0, 255, 0, 20),
        },
        "violet": {
            "normal": QColor(172, 32, 218, 255),
            "hover": QColor(172, 32, 218, 60),
            "click": QColor(172, 32, 218, 20),
        },
        "black": {
            "normal": QColor(0, 0, 0, 255),
            "hover": QColor(0, 0, 0, 60),
            "click": QColor(0, 0, 0, 20),
        },
        "white": {
            "normal": QColor(255, 255, 255, 255),
            "hover": QColor(255, 255, 255, 60),
            "click": QColor(255, 255, 255, 20),
        },
        "gold": {
            "normal": QColor(218, 165, 32, 255),
            "hover": QColor(218, 165, 32, 60),
            "click": QColor(218, 165, 32, 20),
        },
    }
    if buttoncolor is not None and buttoncolor in combos:
        return combos[buttoncolor]


def create_icon_variaties(icon_path: str, color_combo):
    original_pixmap = QPixmap(icon_path)

    normal_icon = change_color_of_pixmap(original_pixmap, color_combo["normal"])
    hover_icon = change_color_of_pixmap(original_pixmap, color_combo["hover"])
    click_icon = change_color_of_pixmap(original_pixmap, color_combo["click"])

    return normal_icon, hover_icon, click_icon


def change_color_of_pixmap(pixmap, new_color):
    # Erstellen eines neuen Pixmap in der gleichen Größe wie das Original
    colored_pixmap = QPixmap(pixmap.size())
    colored_pixmap.fill(Qt.transparent)

    # Verwenden von QPainter, um die Farbe zu ändern
    painter = QPainter(colored_pixmap)
    painter.setCompositionMode(QPainter.CompositionMode_Source)
    painter.drawPixmap(0, 0, pixmap)
    painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
    painter.fillRect(colored_pixmap.rect(), new_color)
    painter.end()

    return colored_pixmap

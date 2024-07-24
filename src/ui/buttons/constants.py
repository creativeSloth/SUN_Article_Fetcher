import os
from typing import Dict

from PyQt5.QtGui import QColor

from directories.constants import DIRS, ICONS_FOLDER


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


def get_paths_of_icons(icon_name: str = None) -> str:
    icon_folder_path: str = DIRS.paths[ICONS_FOLDER]
    default_color_appendix: str = "_48dp_WHITE.png"

    if icon_name is not None:
        button_icon_path: str = os.path.join(
            icon_folder_path, f"{icon_name}{default_color_appendix}"
        )
        button_icon_path = button_icon_path.replace("\\", "/")
    else:
        button_icon_path = None

    return button_icon_path


def create_button_type_map():
    return {
        "doc_available": (get_paths_of_icons("documents"), get_color_combo("gold")),
        "move_to_bl": (get_paths_of_icons("list_remove"), get_color_combo("red")),
        "move_from_bl": (get_paths_of_icons("list_add"), get_color_combo("green")),
        "search": (get_paths_of_icons("search"), get_color_combo("blue")),
        "open_bl": (get_paths_of_icons("preview_off"), get_color_combo("black")),
        "load_articles_db": (get_paths_of_icons("database"), get_color_combo("red")),
        "load_articles_file": (
            get_paths_of_icons("home_storage"),
            get_color_combo("red"),
        ),
        "target_path": (get_paths_of_icons("drive_folder"), get_color_combo("blue")),
    }


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

    return PB_MAP

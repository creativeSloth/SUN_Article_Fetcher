from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QPainter, QColor
from PyQt5.QtCore import Qt, QEvent
import os

from directories.directory_base import MAIN_PATHS
from tables.search_bar import SEARCH_BUTTON_LIST


def get_paths_of_icons(icon_name: str = None):
    icon_folder_path = MAIN_PATHS.dict['icons_folder_path']

    default_color_appendix = '_48dp_WHITE.png'

    if icon_name is not None:
        button_icon_path = (os.path.join(
            icon_folder_path, f'{icon_name}{default_color_appendix}'))

    return button_icon_path


def get_button_icons(self):

    PB_MAP = {
        self.ui.load_articles_db_btn: get_paths_of_icons('database'),
        self.ui.load_articles_file_btn: get_paths_of_icons('home_storage'),
        self.ui.target_path_btn: get_paths_of_icons('drive_folder'),
        self.ui.paste_docs_btn: get_paths_of_icons('file_copy'),
        self.ui.load_data_to_device_lists_btn: get_paths_of_icons('list_alt')
    }
    for button in SEARCH_BUTTON_LIST:
        PB_MAP[button] = get_paths_of_icons('search')

    return PB_MAP


def customize_push_buttons(self):
    # Setze die Icons und füge Event-Filter hinzu
    PB_MAP = get_button_icons(self)
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
    colored_PB_MAP = {}
    for button, icon_path in PB_MAP.items():
        normal_icon, hover_icon, click_icon = create_icon_variaties(
            icon_path)
        colored_PB_MAP[button] = (normal_icon, hover_icon, click_icon)

    return colored_PB_MAP


def create_icon_variaties(icon_path):
    original_pixmap = QPixmap(icon_path)
    normal_color = QColor(19, 33, 59, 255)
    hover_color = QColor(19, 33, 59, 100)
    click_color = QColor(19, 33, 59, 50)
    normal_icon = change_color_of_pixmap(original_pixmap, normal_color)
    hover_icon = change_color_of_pixmap(original_pixmap, hover_color)
    click_icon = change_color_of_pixmap(original_pixmap, click_color)

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


def eventFilter(self, source, event: QEvent):
    if isinstance(source, QPushButton):
        if event.type() == QEvent.Enter:
            source.setIcon(source.hover_icon)
        elif event.type() == QEvent.Leave:
            source.setIcon(source.normal_icon)
        elif event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            source.setIcon(source.click_icon)

    return False

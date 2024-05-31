from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QEvent
import os

from directories.directory_base import MAIN_PATHS


def get_button_icons(self):
    icon_folder_path = MAIN_PATHS.dict['icons_folder_path']
    normal_color_appendix = '_48dp_#13213B.png'
    hover_color_appendix = '_48dp_#13213B95.png'
    press_color_appendix = '_48dp_#13213B50.png'

    PB_MAP = {
        self.ui.load_articles_db_btn: (os.path.join(
            icon_folder_path, f'database{normal_color_appendix}'),
            os.path.join(
            icon_folder_path, f'database{hover_color_appendix}'),
            os.path.join(
            icon_folder_path, f'database{press_color_appendix}')),

        self.ui.load_articles_file_btn: (os.path.join(
            icon_folder_path, f'home_storage{normal_color_appendix}'),
            os.path.join(
            icon_folder_path, f'home_storage{hover_color_appendix}'),
            os.path.join(
            icon_folder_path, f'home_storage{press_color_appendix}')),
    }
    return PB_MAP


def customize_push_buttons(self):
    # Setze die Icons und füge Event-Filter hinzu
    PB_MAP = get_button_icons(self)
    for button, icons in PB_MAP.items():
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


def eventFilter(self, source, event: QEvent):
    if isinstance(source, QPushButton):
        if event.type() == QEvent.Enter:
            source.setIcon(source.hover_icon)
        elif event.type() == QEvent.Leave:
            source.setIcon(source.normal_icon)
        elif event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            source.setIcon(source.click_icon)

    return False

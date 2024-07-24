from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap


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


def create_icon_variaties(icon_path: str, color_combo):
    original_pixmap = QPixmap(icon_path)
    normal_icon = change_color_of_pixmap(original_pixmap, color_combo["normal"])
    hover_icon = change_color_of_pixmap(original_pixmap, color_combo["hover"])
    click_icon = change_color_of_pixmap(original_pixmap, color_combo["click"])

    return normal_icon, hover_icon, click_icon


def create_colored_PB_MAP(PB_MAP: dict):
    colored_PB_MAP: dict = {}
    for button, value in PB_MAP.items():
        icon_path, color_combo = value
        normal_icon, hover_icon, click_icon = create_icon_variaties(
            icon_path, color_combo
        )
        colored_PB_MAP[button] = (normal_icon, hover_icon, click_icon)

    return colored_PB_MAP

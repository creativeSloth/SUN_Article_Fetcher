from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtWidgets import QPushButton, QTableWidget, QTextEdit


def mouse_enters_pb(event):
    return event.type() == QEvent.Enter


def mouse_leaves_pb(event):
    return event.type() == QEvent.Leave


def lmbutton_presses(event):

    return event.type() == QEvent.MouseButtonPress and event.buttons() == Qt.LeftButton


def enter_key_pressed(event):
    return event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return


def lmbutton_releases_pb(event):
    return (
        event.type() == QEvent.MouseButtonRelease
        and event.type() != QEvent.Leave
        and event.button() == Qt.LeftButton
    )


def is_pushbutton(source):
    return isinstance(source, QPushButton)


def is_table(source):
    return isinstance(source, QTableWidget)


def is_search_box(source):
    return (
        isinstance(source, QTextEdit)
        and getattr(source, "text_edit_type", None) is not None
    )

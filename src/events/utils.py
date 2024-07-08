from PyQt5.QtCore import QEvent, Qt


def mouse_enters_pb(event):
    return event.type() == QEvent.Enter


def mouse_leaves_pb(event):
    return event.type() == QEvent.Leave


def lmbutton_presses_pb(event):
    return event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton


def enter_key_pressed(event):
    return event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return


def lmbutton_releases_pb(event):
    return (
        event.type() == QEvent.MouseButtonRelease
        and event.type() != QEvent.Leave
        and event.button() == Qt.LeftButton
    )

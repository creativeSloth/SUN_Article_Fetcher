from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtWidgets import QPlainTextEdit, QWidget

from events.utils import (
    enter_key_pressed,
    is_pushbutton,
    is_search_box,
    lmbutton_presses,
    lmbutton_releases_pb,
    mouse_enters_pb,
    mouse_leaves_pb,
)


def event_Filter(self, source: QWidget = None, event: QEvent = None) -> bool:
    if is_pushbutton(source):
        if mouse_enters_pb(event):
            source.setIcon(source.hover_icon)
        elif mouse_leaves_pb(event):
            source.setIcon(source.normal_icon)
        elif lmbutton_presses(event):
            source.setIcon(source.click_icon)
        elif lmbutton_releases_pb(event):
            source.setIcon(source.hover_icon)

    # Prüfe, ob das Ereignis von einem QTextEdit kommt
    if is_search_box(source):
        if enter_key_pressed(event):
            table = getattr(source, "table", None)
            if table is not None:
                func = getattr(source, "func", None)
                if func:
                    func(self, table=table, text_edit=source)
                    return True
    # if source.objectName() == "project" and isinstance(source, QPlainTextEdit):
    #     if lmbutton_presses(event):
    #         print("hi")
    #         # Event ignorieren, um das Scrollen zu verhindern
    #         return False
    #     elif event.type() == QEvent.MouseMove and event.buttons() & Qt.LeftButton:
    #         # Mausbewegungen beim Drücken der linken Maustaste ignorieren
    #         return False
    #     elif (
    #         event.type() == QEvent.MouseButtonRelease
    #         and event.button() == Qt.LeftButton
    #     ):
    #         # Mausfreigabe-Ereignis behandeln, wenn nötig
    #         pass

    return False

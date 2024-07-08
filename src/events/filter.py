from typing import Any

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QPushButton

from events.utils import (
    enter_key_pressed,
    lmbutton_presses_pb,
    lmbutton_releases_pb,
    mouse_enters_pb,
    mouse_leaves_pb,
)
from ui.tables.search_bar import is_search_box


def event_Filter(self, source: Any = None, event: QEvent = None):
    if isinstance(source, QPushButton):
        if mouse_enters_pb(event):
            source.setIcon(source.hover_icon)
        elif mouse_leaves_pb(event):
            source.setIcon(source.normal_icon)
        elif lmbutton_presses_pb(event):
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
                    func(table, source)
                    return True

    return False

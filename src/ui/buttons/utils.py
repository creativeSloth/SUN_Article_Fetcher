from typing import Any, List, Type

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QTableWidget, QWidget


def create_and_set_obj_property(
    obj: Any, property_type: str = None, property_value: Any = None
) -> Any:
    if property_type is not None:
        setattr(obj, property_type, property_value)
        obj.setProperty(property_type, property_value)
    return obj


def list_objects_of_class(parent: QWidget, cls: Type) -> List[Type]:
    objects = parent.findChildren(cls)
    return objects


def list_of_property_members(
    property_type: str = None, property_value: str = "", wanted_objs: list = None
) -> List[Type]:
    return [
        obj
        for obj in wanted_objs
        if getattr(obj, property_type, None) == property_value
    ]


def set_pushbutton_for_cell(
    self,
    table_of_cell: QTableWidget,
    row: int,
    column: int,
    button_type: str,
    on_button_pressed: Any,
):
    setattr(
        self,
        f"push_button_{table_of_cell.objectName()}_{row}_{column}",
        QPushButton(""),
    )
    push_button: QPushButton = getattr(
        self, f"push_button_{table_of_cell.objectName()}_{row}_{column}", None
    )
    push_button.setObjectName(
        f"push_button_{table_of_cell.objectName()}_{row}_{column}"
    )
    create_and_set_obj_property(
        obj=push_button, property_type="button_type", property_value=button_type
    )

    push_button.setFixedSize(25, 25)

    if on_button_pressed:
        push_button.clicked.connect(
            lambda _, tbl=table_of_cell, btn=push_button: on_button_pressed(
                self, tbl, btn
            )
        )

    return push_button


def set_cell_widget(table_of_cell, row, column, push_button):
    layout: QHBoxLayout
    cell_widget: QWidget = table_of_cell.cellWidget(row, column)
    if cell_widget is None:
        cell_widget = QWidget()
        layout = QHBoxLayout()
        layout.setObjectName(f"Layout_{table_of_cell.objectName()}_{row}_{column}")
        layout.setContentsMargins(7, 2, 7, 2)
        layout.setSpacing(2)
        cell_widget.setLayout(layout)

    cell_widget.layout().addWidget(push_button)
    create_and_set_obj_property(
        obj=cell_widget,
        property_type="cell_widget",
        property_value="contains_push_button",
    )

    return cell_widget


def set_icon_event_behavior(self, pb, icon_varieties):
    normal_icon_path, hover_icon_path, click_icon_path = icon_varieties
    pb.setIcon(QIcon(normal_icon_path))
    pb.setIconSize(pb.size())

    # Icons als Button-Attribute speichern
    pb.normal_icon = QIcon(normal_icon_path)
    pb.hover_icon = QIcon(hover_icon_path)
    pb.click_icon = QIcon(click_icon_path)

    # Event-Filter hinzufügen
    pb.installEventFilter(self)

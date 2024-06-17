from typing import Any, List, Type

from PyQt5.QtWidgets import QWidget


def create_and_set_obj_property(
    obj: Any, property_type: str = None, property_value: Any = None
) -> Any:
    if property_type is not None:
        setattr(obj, property_type, property_value)
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

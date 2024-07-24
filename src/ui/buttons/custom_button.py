from ui.buttons.constants import (
    create_button_type_map,
    get_button_icons_color_connected,
)
from ui.buttons.constants_helpers import create_colored_PB_MAP, create_icon_variaties
from ui.buttons.utils import set_icon_event_behavior


def customize_static_pb(self):
    self.button_list.refresh()

    # Setze die Icons und füge Event-Filter hinzu
    PB_MAP = get_button_icons_color_connected(self)
    colored_PB_MAP = create_colored_PB_MAP(PB_MAP)

    for pb, icon_varieties in colored_PB_MAP.items():
        # Standard-Icon setzen
        set_icon_event_behavior(self, pb, icon_varieties)


def customize_dynamic_pb(self, pb):
    BUTTON_TYPE_MAP = create_button_type_map()
    button_type = getattr(pb, "button_type", None)
    if button_type in BUTTON_TYPE_MAP:
        icon_path, color_combo = BUTTON_TYPE_MAP[button_type]
    icon_varieties = create_icon_variaties(icon_path, color_combo)
    set_icon_event_behavior(self, pb, icon_varieties)

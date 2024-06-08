from ui.fields.ui_fields_base import get_all_tables
from ui.tables.tables_base import on_sort_indicator_changed


def connect_sort_indicator_changed(self):
    tables = get_all_tables(self)
    for table in tables:
        # Verwendung von lambda-Funktion, um das Argument "table" zu übergeben
        table.horizontalHeader().sortIndicatorChanged.connect(
            lambda sortIndex, order, table=table: on_sort_indicator_changed(
                self, table=table
            )
        )

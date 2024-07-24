from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox, QTableWidget


def change_foreground_if_zero(table: QTableWidget):
    if table.objectName() == "blacklist":
        return
    for row in range(table.rowCount()):
        amount_item = table.item(row, 3)
        count: float = amount_item.text()
        try:
            if amount_item is None or float(count) != 0:
                continue

            for column in range(1, table.columnCount()):
                if table.item(row, column) is None:
                    continue
                table.item(row, column).setForeground(QColor("#e20000"))
                setattr(table.item(row, column), "property", "isZero")

        except ValueError:
            pass


def customize_table_row(func):
    def wrapper(self, *args, **kwargs):
        if "table" in kwargs:
            table = kwargs["table"]
        elif "bl_table" in kwargs:
            table = kwargs["bl_table"]

        if table is not None:
            table.setSortingEnabled(False)

        func(self, *args, **kwargs)  # Rufe die ursprüngliche Funktion auf

        if table is not None:
            table.setSortingEnabled(True)

        from ui.tables.utils import on_table_view_changed

        on_table_view_changed(self, table=table)
        # Führe die Anpassung der Zeilenfarben durch
        change_foreground_if_zero(table)

    return wrapper

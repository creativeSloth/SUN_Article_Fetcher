from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox


def change_foreground_if_zero(table):

    for row in range(table.rowCount()):
        count: float = table.item(row, 3).text()
        try:
            if table.item(row, 3) is not None and float(count) == 0:

                for column in range(1, table.columnCount()):
                    if table.item(row, column) is not None:
                        table.item(row, column).setForeground(QColor("#e20000"))
        except ValueError:
            pass


def customize_table_row(func):
    def wrapper(self, *args, **kwargs):

        table = kwargs["table"]

        if table is not None:
            table.setSortingEnabled(False)

        func(self, *args, **kwargs)  # Rufe die ursprüngliche Funktion auf

        if table is not None:

            table.setSortingEnabled(True)

            # Führe die Anpassung der Zeilenfarben durch
            change_foreground_if_zero(table)
        else:
            # Wenn table None ist, gebe eine Fehlermeldung aus
            QMessageBox.information(
                self,
                "Entwicklerinfo",
                f"Die Zeilenfarbe wird nicht geändert.\n"
                "def change_table_row_colour(func):\n"
                "table = kwargs['table'] --> None",
            )

    return wrapper

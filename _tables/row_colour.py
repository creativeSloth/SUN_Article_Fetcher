from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui


def customize_table_row(func):
    def wrapper(self, *args, **kwargs):

        table = kwargs['table']
        # table = None --> Für Entwicklertests

        if table is not None:
            table.setSortingEnabled(False)

        func(self, *args, **kwargs)  # Rufe die ursprüngliche Funktion auf

        if table is not None:
            table.setSortingEnabled(True)

            # Führe die Anpassung der Zeilenfarben durch
            for row in range(table.rowCount()):
                count = table.item(row, 3).text()
                for column in range(table.columnCount()):

                    change_foreground_if_zero(
                        count, table, row, column)
                    change_background_colour(table, row, column)
        else:
            # Wenn table None ist, gebe eine Fehlermeldung aus
            QMessageBox.information(
                self, "Entwicklerinfo", f"Die Zeilenfarbe wird nicht geändert.\n"
                                        "def change_table_row_colour(func):\n"
                                        "table = kwargs['table'] --> None")

    return wrapper


def change_foreground_if_zero(count, table, row, column):
    if float(count) == 0:
        for column in range(1, table.columnCount()):
            table.item(row, column).setForeground(
                QtGui.QColor("#e20000"))


def change_background_colour(table, row, column):
    if row % 2 == 0:
        table.item(row, column).setBackground(QtGui.QColor(
            "#F6A4A4"))  # Hintergrundfarbe für gerade Zeilen
    else:
        # Hintergrundfarbe für ungerade Zeilen
        table.item(row, column).setBackground(
            QtGui.QColor("#BAE290"))

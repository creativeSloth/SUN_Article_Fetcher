from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui


def change_table_row_colour(func):
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
                for column in range(table.columnCount()):
                    if row % 2 == 0:
                        table.item(row, column).setBackground(QtGui.QColor(
                            "#F6A4A4"))  # Hintergrundfarbe für gerade Zeilen
                    else:
                        # Hintergrundfarbe für ungerade Zeilen
                        table.item(row, column).setBackground(
                            QtGui.QColor("#BAE290"))
        else:
            # Wenn table None ist, gebe eine Fehlermeldung aus
            QMessageBox.information(
                self, "Entwicklerinfo", f"Die Zeilenfarbe wird nicht geändert.\n"
                                        "def change_table_row_colour(func):\n"
                                        "table = kwargs['table'] --> None")

    return wrapper

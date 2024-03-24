import pandas as pd
from PyQt5.QtWidgets import QTextEdit, QHBoxLayout, QVBoxLayout, QSizePolicy, QPushButton
import ui_fields_Handler


def set_all_table_headers(self):
    tables = ui_fields_Handler.get_device_tables(self)

    for table in tables:
        button, text_edit = add_table_header_search_box(
            table=table, layout=self.ui.verticalLayout_3)
        init_search_button_click_signal(table=table,
                                        button=button,
                                        text_edit=text_edit)

    tables = ui_fields_Handler.get_articles_table(self)
    for table in tables:
        button, text_edit = add_table_header_search_box(
            table=table, layout=self.ui.verticalLayout)
        init_search_button_click_signal(table=table,
                                        button=button,
                                        text_edit=text_edit)


def add_table_header_search_box(table, layout):
    index = layout.indexOf(table)

    # QHBoxLayout erstellen, um die Suchleiste nebeneinander anzuordnen
    search_layout = QHBoxLayout()
    max_height = 25

    # QLabel für die Suchleiste erstellen und hinzufügen
    button = QPushButton("Suchen")
    button.setStyleSheet("text-decoration: underline;")
    button.setMaximumHeight(max_height)  # Maximale Höhe auf 30 setzen
    button.setMinimumWidth(150)  # Maximale Breite auf
    button.setObjectName(table.objectName() + "_search_button")
    search_layout.addWidget(button)

    # QTextEdit für die Suchleiste erstellen und hinzufügen
    text_edit = QTextEdit()
    text_edit.setMaximumHeight(max_height)  # Maximale Höhe auf 30 setzen
    # Objektname ableiten und zuweisen
    text_edit.setObjectName(table.objectName() + "_search_text_edit")
    search_layout.addWidget(text_edit)

    # QHBoxLayout für die Tabelle erstellen und die Tabelle hinzufügen
    table_layout = QHBoxLayout()
    table_layout.addWidget(table)

    # QVBoxLayout für die Kombination von Suchleiste und Tabelle erstellen
    comb_search_layout = QVBoxLayout()

    # Suchleiste in den kombinierten Layout einfügen
    comb_search_layout.insertLayout(0, search_layout)

    # Tabelle in den kombinierten Layout einfügen
    comb_search_layout.addLayout(table_layout)
    # Horizontal und Vertikal dehnen
    table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    # Kombiniertes Layout an der ursprünglichen Position einfügen
    layout.insertLayout(index, comb_search_layout)
    return button, text_edit


def init_search_button_click_signal(table, button, text_edit):
    button.clicked.connect(
        lambda: on_search_button_click(table=table,
                                       button=button,
                                       text_edit=text_edit
                                       ))


def on_search_button_click(table, button, text_edit):

    search_string = text_edit.toPlainText()

    print(text_edit.objectName())
    print(button.objectName())
    print(search_string)

    hide_rows_without_string(table, search_string)


def hide_rows_without_string(table, search_string):
    # Konvertieren Sie den Suchstring in Kleinbuchstaben
    search_string_lower = search_string.lower()

    for row in range(table.rowCount()):
        found = False
        for col in range(table.columnCount()):
            item = table.item(row, col)
            if item is not None:
                # Konvertieren Sie den Text des Elements in Kleinbuchstaben und prüfen Sie auf das Vorhandensein des Suchstrings
                if isinstance(item.text(), str) and search_string_lower in item.text().lower():
                    found = True
                    break
                elif isinstance(item.text(), float) and search_string_lower in str(item.text()).lower():
                    found = True
                    break
        table.setRowHidden(row, not found)

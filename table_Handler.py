from tkinter import HORIZONTAL
from PyQt5.QtWidgets import QTextEdit, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy
import ui_fields_Handler


def set_all_table_headers(self):
    tables = ui_fields_Handler.get_device_tables(self)
    for table in tables:
        add_table_header_search_box(
            table=table, layout=self.ui.verticalLayout_3)
    tables = ui_fields_Handler.get_articles_table(self)
    for table in tables:
        add_table_header_search_box(
            table=table, layout=self.ui.verticalLayout)


def add_table_header_search_box(table, layout):
    index = layout.indexOf(table)

    # QHBoxLayout erstellen, um die Suchleiste nebeneinander anzuordnen
    search_layout = QHBoxLayout()

    # QLabel für die Suchleiste erstellen und hinzufügen
    label = QLabel("Suche:")
    search_layout.addWidget(label)

    # QTextEdit für die Suchleiste erstellen und hinzufügen
    text_edit = QTextEdit()
    text_edit.setMaximumHeight(25)  # Maximale Höhe auf 30 setzen
    text_edit.setObjectName(table.objectName() + "_search_text_edit")  # Objektname ableiten und zuweisen
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
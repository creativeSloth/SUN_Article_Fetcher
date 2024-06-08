from PyQt5.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QSizePolicy,
    QTextEdit,
    QVBoxLayout,
)


def add_table_header_search_box(self, table, layout):
    index = layout.indexOf(table)

    # QHBoxLayout erstellen, um die Suchleiste nebeneinander anzuordnen
    search_layout = QHBoxLayout()
    search_layout.setSpacing(5)
    search_layout.setContentsMargins(0, 0, 0, 5)
    min_height = 30
    max_height = 30
    min_width = 30
    max_width = 30

    # QLabel für die Suchleiste erstellen und hinzufügen
    button = QPushButton("")
    # button.setStyleSheet("text-decoration: underline;")
    button.setMinimumHeight(min_height)
    button.setMaximumHeight(max_height)
    button.setMinimumWidth(min_width)
    button.setMaximumWidth(max_width)
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

    self.button_list.add_generic_button(button=button, button_type="search")

    return button, text_edit


def init_search_button_click_signal(table, button, text_edit):
    button.clicked.connect(
        lambda: on_search_button_click(table=table, text_edit=text_edit)
    )


def on_search_button_click(table, text_edit):

    search_string = text_edit.toPlainText()
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
                if (
                    isinstance(item.text(), str)
                    and search_string_lower in item.text().lower()
                ):
                    found = True
                    break
                elif (
                    isinstance(item.text(), float)
                    and search_string_lower in str(item.text()).lower()
                ):
                    found = True
                    break
        table.setRowHidden(row, not found)

from PyQt5.QtWidgets import QTableWidgetItem, QToolButton, QHBoxLayout, QLineEdit, QWidget, QHeaderView
import ui_fields_Handler


def set_all_table_headers(self):
    tables = ui_fields_Handler.get_all_tables(self)
    for table in tables:
        for column in range(table.columnCount()):
            set_table_header_search_box(table=table, column=column)


def set_table_header_search_box(table, column):
    # Einfügen einer Zeile, wenn die Tabelle leer ist
    if table.rowCount() == 0:
        table.insertRow(0)

    # Holen Sie sich den vorhandenen Text des Spaltenkopfes für die angegebene Spalte
    column_header_text = table.horizontalHeaderItem(column).text()

    if column_header_text.endswith('Typ') or column_header_text in ['Artikelnummer', 'Artikelbezeichnung']:

        # Erstellen Sie ein benutzerdefiniertes Widget für den Header der Spalte
        header_widget = QWidget()

        # Erstellen Sie ein Layout für das benutzerdefinierte Widget
        layout = QHBoxLayout(header_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Erstellen Sie ein QLineEdit für den Spaltenkopftext und fügen Sie es zum Layout hinzu
        header_line_edit = QLineEdit()
        # Setzen Sie die minimale Breite des QLineEdit
        header_line_edit.setMinimumWidth(200)
        layout.addWidget(header_line_edit)

        # Erstellen Sie die Suchschaltfläche (QToolButton)
        search_button = QToolButton()
        # Setzen Sie optional den Text für die Schaltfläche
        search_button.setText("Search")
        # Hier kannst du die Schaltfläche nach deinen Bedürfnissen anpassen, z.B. Icon hinzufügen usw.

        # Fügen Sie die Schaltfläche zum Layout hinzu
        layout.addWidget(search_button)

        # Setzen Sie das Layout für das benutzerdefinierte Widget
        header_widget.setLayout(layout)

        # Setzen Sie das benutzerdefinierte Widget als Kopfzeilen-Element für die Spalte
        table.setHorizontalHeaderItem(column, QTableWidgetItem())
        table.setHorizontalHeaderItem(column, QTableWidgetItem(
            column_header_text))  # Spaltenkopftext einsetzen
        # Annahme: Das benutzerdefinierte Widget wird in der ersten Zeile der Kopfzeile platziert
        table.setCellWidget(0, column, header_widget)
        # Die erste Zeile einfrieren
        table.verticalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        # Automatisches Anpassen der Breite der Spalte 0 an den Inhalt
        table.resizeColumnToContents(column)

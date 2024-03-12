import sys
import os
import shutil

from odf.opendocument import load
from odf import text, teletype
from odf.table import Table, TableRow, TableCell

import pandas as pd
from sqlalchemy import create_engine

from qtpy import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from ui.mainwindow import Ui_MainWindow
from decorators import get_file_path, get_folder_path, check_path_existence
import directory_Handler
import ui_fields_Handler
import logs_and_config


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,
                 parent=None):
        super().__init__(parent)

        # Erstelle eine Instanz der Benutzeroberfläche aus der generierten Ui-Datei
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("SUN-DOC")
        # Variablen df und sql_query als Instanzvariable initialisieren
        self.initialize()
        # Verbinde die Signale mit den entsprechenden Slots
        self.map_ui_buttons()
        logs_and_config.create_config_file(self)
        ui_fields_Handler.config_to_fields(self)

    def map_ui_buttons(self):

        #  *********************************** Mapping buttons for "Article Fetcher"-module *****************************************

        self.ui.load_articles_file_btn.clicked.connect(
            self.on_load_articles_from_file_btn_click)
        self.ui.load_articles_db_btn.clicked.connect(
            self.on_load_articles_from_db_btn_click)
        self.ui.source_path_btn.clicked.connect(
            self.on_source_path_btn_click)
        self.ui.target_path_btn.clicked.connect(
            self.on_target_path_btn_click)
        self.ui.paste_docs_btn.clicked.connect(
            self.on_copy_files_btn_click)
        self.ui.sql_query_btn.clicked.connect(
            self.on_sql_query_btn_click)

        self.ui.articles_list.horizontalHeader(
        ).sortIndicatorChanged.connect(self.sort_table)

        #  *********************************** Mapping buttons for "Documentation"- module *****************************************
        self.ui.source_btn_matstr.clicked.connect(
            self.on_source_btn_matstr_click)
        self.ui.source_btn_docu.clicked.connect(
            self.on_source_btn_docu_click)
        self.ui.target_path_btn_2.clicked.connect(
            self.on_target_path_btn_2_click)
        self.ui.create_docs_btn.clicked.connect(
            self.on_btn_create_docs_clicked)

    def sort_table(self, column, order):
        self.ui.articles_list.sortItems(column, order)

    def initialize(self):
        # set default values
        self.df = None
        self.sql_query = None

        # query_input-Box verstecken
        self.ui.query_input.hide()
        self.ui.query_2_input.hide()

    def on_load_articles_from_file_btn_click(self):
        # Öffne einen Dateiauswahldialog für Benutzer
        file_dialog = QFileDialog()
        file_dialog.setNameFilter(
            "CSV Files (*.csv);;Excel Files (*.xlsx);;Libre Calc Files (*.ods)")

        # Überprüfen Sie, ob der Benutzer "OK" gedrückt hat
        if file_dialog.exec_() == QFileDialog.Accepted:
            # Erhalte den ausgewählten Dateipfad
            file_path = file_dialog.selectedFiles()[0]

            # Führe hier den nachfolgenden Code aus, wenn "OK" gedrückt wurde
            # Überprüfen Sie zusätzlich, ob file_path nicht leer ist
            if file_path:
                # Lösche die vorhandenen Daten und fülle die Tabelle mit Daten aus der Datei
                self.clear_article_list()
                self.fill_article_list(file_path=file_path, df=None)

    def on_load_articles_from_db_btn_click(self):
        # Lese Daten aus der MySQL-Datenbank und speichere sie in der Instanzvariable df
        self.df = self.read_sql()
        # Lösche die vorhandenen Daten und fülle die Tabelle mit den Daten aus der Datenbank
        self.clear_article_list()
        self.fill_article_list(file_path=None, df=self.df)

    @get_folder_path
    def on_source_path_btn_click(self, folder_path):
        self.ui.source_path_text.setPlainText(folder_path)
        logs_and_config.update_config_file(
            self, 'Pfade', 'source_path', folder_path)

    @get_folder_path
    def on_target_path_btn_click(self, folder_path):
        self.ui.target_path_text.setPlainText(folder_path)
        logs_and_config.update_config_file(
            self, 'Pfade', 'target_path', folder_path)

    @ check_path_existence(modus=0)
    def on_copy_files_btn_click(self, *args, **kwargs):
        # Holen Sie sich Pfade für Quell- und Zielordner aus den Textfeldern
        source_path = directory_Handler.get_directories(self)[
            'source_path']
        target_path = directory_Handler.get_directories(self)[
            'target_path_1']
        log_sub2folder_path = directory_Handler.get_directories(self)[
            'log_sub2folder_path']

        # Holen Sie sich alle Dateinamen im source_path
        source_files = self.get_files_in_source_path(source_path)

        # Holen Sie sich alle ausgewählten Dateien im Table Widget
        selected_files = []
        for row in range(self.ui.articles_list.rowCount()):
            checkbox_item = self.ui.articles_list.item(row, 0)
            filename_item = self.ui.articles_list.item(row, 1)

            # Überprüfe, ob die Checkbox in der aktuellen Zeile angehakt ist
            if checkbox_item and checkbox_item.checkState() == QtCore.Qt.Checked:
                filename = filename_item.text()
                selected_files.append(filename)

        selected_files = list(set(selected_files))

        # Holen Sie sich alle Dateinamen im Quellordner, die den ausgewählten Dateien entsprechen
        matching_files = []
        matching_files = [file for file in source_files if
                          any(selected_file in file for selected_file in selected_files)]

        # Iteriere über alle übereinstimmenden Dateinamen
        count = 0
        for matching_filename in matching_files:
            # Konstruiere den vollständigen Pfad zur Quelldatei
            source_file_path = os.path.join(source_path, matching_filename)

            # Konstruiere den vollständigen Pfad zum Ziel
            target_file_path = os.path.join(target_path, matching_filename)
            target_file_path_ext = os.path.dirname(target_file_path)
            try:
                if not os.path.exists(target_file_path_ext):
                    os.makedirs(target_file_path_ext)

            except Exception as e:
                QtWidgets.QMessageBox.warning(
                    self, "Fehler", f"Fehler beim Erstellen des Verzeichnisses {target_file_path.root()}.\n\n"
                                    f"Fehler: {e}")

            # Kopiere die Datei
            try:
                shutil.copy(source_file_path, target_file_path)
                count += 1
            except Exception as e:
                QtWidgets.QMessageBox.warning(
                    self, "Fehler", f"Fehler beim Kopieren der Datei {source_file_path} zu {target_file_path}.\n\n"
                                    f"Fehler: {e}")

        # Rufen Sie die separate Funktion für das Logging auf
        logs_and_config.log_copy_details(self, source_path, target_path,
                                         source_files, matching_files)

        # Gib eine Erfolgsmeldung aus
        QtWidgets.QMessageBox.information(self, "Erfolg!",
                                          f"Das Kopieren der Dateien wurde beendet.\n"
                                          f"Es wurden insgesamt {count} Dateien übertragen.\n\n"
                                          f"Es wurde eine Logdatei im log-Ordner:\n\n {log_sub2folder_path}\n\n erstellt.")

    def fill_article_list(self, file_path=None, df=None):

        if file_path is not None and df is None:
            # Wenn ein Dateipfad übergeben wurde, lese Daten aus der Datei
            df = self.read_data(file_path)

        if df is not None:
            for index, row in df.iterrows():
                tw_row = self.ui.articles_list.rowCount()
                self.ui.articles_list.insertRow(tw_row)

                # Spalte 1 (statisch) mit einer Checkbox
                checkbox_item = QtWidgets.QTableWidgetItem()
                checkbox_item.setFlags(
                    QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                checkbox_item.setCheckState(QtCore.Qt.Checked)
                self.ui.articles_list.setItem(tw_row, 0, checkbox_item)

                # Spalte 2 (dynamisch) mit den Werten aus der Spalte 0 des DataFrames
                item_col1 = QtWidgets.QTableWidgetItem(str(row.iloc[0]))
                self.ui.articles_list.setItem(tw_row, 1, item_col1)
                # Spalte 3 (dynamisch) mit den Werten aus der Spalte 1 des DataFrames
                item_col2 = QtWidgets.QTableWidgetItem(str(row.iloc[1]))
                self.ui.articles_list.setItem(tw_row, 2, item_col2)

        # Iteriere über alle Zellen im Table Widget
        for row in range(self.ui.articles_list.rowCount()):
            for col in range(1, self.ui.articles_list.columnCount()):
                item = self.ui.articles_list.item(row, col)
                if item:
                    # Deaktiviere die Editierbarkeit für die Zelle
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

        self.resize_columns_to_contents()

        QtWidgets.QMessageBox.information(
            self, "Abgeschlossen!", "Liste geladen!")

    def get_files_in_source_path(self, directory):
        all_files = []

        try:
            for root, _, files in os.walk(directory):
                for file in files:
                    try:
                        file_path = os.path.relpath(
                            os.path.join(root, file), directory)
                        all_files.append(file_path)

                    except Exception as e:
                        QtWidgets.QMessageBox.warning(self, "Fehler!",
                                                      f"Die Datei für {file_path} konnte nicht gelesen werden.\n\n {e}")

            return all_files

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Fehler!",
                                          f"Die Datei für {directory} konnte nicht gelesen werden.\n\n {e}")

    def on_sql_query_btn_click(self):

        if self.ui.query_input.isHidden():
            self.ui.query_input.show()
        else:
            self.ui.query_input.hide()

    def clear_article_list(self):
        # Setze die Anzahl der Zeilen auf 0, um alle Zeilen zu entfernen
        self.ui.articles_list.setRowCount(0)

    def read_data(self, file_path):
        if file_path.endswith('.csv'):
            return self.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            return self.read_xlsx(file_path)
        elif file_path.endswith('.ods'):
            return self.read_ods(file_path)

    def read_csv(self, file_path):
        # Lese CSV-Datei und gebe DataFrame zurück
        dtypes = {0: str, 1: str}
        df = pd.read_csv(file_path, header=None, dtype=dtypes)
        df = df.drop_duplicates()
        return df

    def read_xlsx(self, file_path):
        # Lese Excel-Datei und gebe DataFrame zurück
        dtypes = {0: str, 1: str}
        df = pd.read_excel(file_path, header=None, dtype=dtypes)
        df = df.drop_duplicates()
        return df

    def read_ods(self, file_path):
        # Lese Excel-Datei und gebe DataFrame zurück
        dtypes = {0: str, 1: str}
        df = pd.read_excel(file_path, header=None, dtype=dtypes, engine="odf")
        df = df.drop_duplicates()
        return df

    def get_server_info(self):

        server_info = []
        server_info.append(self.ui.db_server.toPlainText())
        server_info.append(self.ui.user.toPlainText())
        server_info.append(self.ui.pw.toPlainText())
        server_info.append(self.ui.db_name.toPlainText())

        return server_info

    def get_project(self):
        return self.ui.project.toPlainText()

    def read_sql(self):
        self.sql_query = self.ui.query_input.toPlainText()
        sql_query = self.ui.query_input.toPlainText()
        db_type = self.ui.db_type.currentText()

        self.server_info = self.get_server_info()

        # Konfiguriere MySQL-Verbindungsinformationen
        server = self.server_info[0]  # "127.0.0.1"
        user = self.server_info[1]  # "root"
        pw = self.server_info[2]  # "12345678"
        dB_name = self.server_info[3]  # "db"

        logs_and_config.update_config_file(self, 'Abfrage', 'sql1', sql_query)
        logs_and_config.update_config_file(self, 'Server', 'server', server)
        logs_and_config.update_config_file(self, 'Server', 'user', user)
        logs_and_config.update_config_file(self, 'Server', 'password', pw)
        logs_and_config.update_config_file(self, 'Server', 'dB_name', dB_name)
        try:

            if db_type == "MySQL":
                # Erstelle eine SQLAlchemy-Engine für MySQL-Verbindung
                engine = create_engine(
                    f"mysql+mysqlconnector://{user}:{pw}@{server}/{dB_name}")
                engine.connect()

            elif db_type == "PostgreSQL":
                # Erstelle eine SQLAlchemy-Engine für PostgreSQL-Verbindung
                engine = create_engine(
                    f"postgresql+psycopg2://{user}:{pw}@{server}/{dB_name}")
                engine.connect()

            else:
                # Fügen Sie hier weitere Datenbanktypen hinzu, wenn benötigt
                raise ValueError(
                    f"Datenbanktyp wird nicht unterstützt: {db_type}")

            # Überprüfe, ob die Verbindung erfolgreich hergestellt wurde

            # Beispiel-SQL-Abfrage
            if self.sql_query is None or self.sql_query == "":
                self.sql_query = "SELECT * FROM articles WHERE project_name = '{{project}}';"
                self.ui.query_input.setPlainText(self.sql_query)

            if "{{project}}" in self.sql_query:
                self.sql_query = self.sql_query.replace(
                    "{{project}}", self.get_project())

            # Verwende pd.read_sql, um die Abfrage auszuführen und die Ergebnisse in einen DataFrame zu lesen
            df = pd.read_sql(self.sql_query, con=engine)
            return df

        except Exception as e:
            # Gib eine Erfolgsmeldung aus
            QtWidgets.QMessageBox.critical(
                self,
                "Verbindungsfehler zur Datenbank",
                f"Fehler bei der Verbindung zur Datenbank: {e}\n\n"
                "Überprüfen Sie die Zugangsinformationen zur SQL-Datenbank!"
            )
            return None

    # Beispiel zum manuellen Einstellen der Spaltenbreite
    def resize_columns_to_contents(self):
        header = self.ui.articles_list.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

    def set_server_info_ui_fields(self, server_info):
        if server_info:
            server, user, pw, db_name = server_info.split(", ")
            if self.ui.db_server.toPlainText() == "":
                self.ui.db_server.setPlainText(server)
            if self.ui.user.toPlainText() == "":
                self.ui.user.setPlainText(user)
            if self.ui.pw.toPlainText() == "":
                self.ui.pw.setPlainText(pw)
            if self.ui.db_name.toPlainText() == "":
                self.ui.db_name.setPlainText(db_name)

# * * * * * * * * * * * * * * * * * Documentation-module * * * * * * * * * * * * * * *
    def on_btn_create_docs_clicked(self):
        ui_fields_Handler.set_field_inputs(self)
        self.replace_field()

    @get_file_path
    def on_source_btn_matstr_click(self, file_path):
        self.ui.source_path_text_matstr.setPlainText(file_path)
        logs_and_config.update_config_file(
            self, 'Pfade', 'template1_path', file_path)

    @get_file_path
    def on_source_btn_docu_click(self, file_path):
        self.ui.source_path_text_docu.setPlainText(file_path)
        logs_and_config.update_config_file(
            self, 'Pfade', 'template2_path', file_path)

    @get_folder_path
    def on_target_path_btn_2_click(self, folder_path):
        self.ui.target_path_text_2.setPlainText(folder_path)
        logs_and_config.update_config_file(
            self, 'Pfade', 'target_path_2', folder_path)

    @check_path_existence(modus=1)
    def replace_field(self):
        # Rufe get_directories auf, um die Pfade zu erhalten
        template1_path = directory_Handler.get_directories(self)[
            'template1_path']
        doc1_path = directory_Handler.get_directories(self)[
            'doc1_path']

        try:
            doc1 = load(template1_path)
            context = ui_fields_Handler.get_context(self)

            # Durchlaufe alle Tabellen in der ODF-Datei
            for table in doc1.getElementsByType(Table):
                # Durchlaufe alle Zeilen in der Tabelle
                for row in table.getElementsByType(TableRow):
                    # Durchlaufe alle Zellen in der Zeile
                    for cell in row.getElementsByType(TableCell):
                        # Text in der Zelle erhalten
                        cell_text = ""
                        for text_node in cell.getElementsByType(text.P):
                            cell_text = teletype.extractText(text_node)

                            # Ersetze die Platzhalter im Text

                            for field_name, field_value in context.items():
                                if field_name in cell_text:
                                    cell_text = cell_text.replace(
                                        field_name, str(field_value))

                             # Erstelle den neuen Textknoten mit dem aktualisierten Text
                            new_text_node = text.P(text=cell_text)

                            # Füge den neuen Textknoten in die Zelle ein
                            cell.addElement(new_text_node)

                            # Entferne den alten Textknoten
                            cell.removeChild(text_node)

            # Entferne die Platzhalter in den doppeltgeschweiften Klammern

            doc1.save(doc1_path)
            QtWidgets.QMessageBox.information(
                self, "Abgeschlossen!",
                f"Die Datei wurde unter folgendem Pfad gespeichert:\n"
                f"{doc1_path}")

        except Exception as e:
            QtWidgets.QMessageBox.warning(
                self, "Fehler", f"Fehler bei der Feldersetzung: {e}")


# Führe das Programm aus, wenn es direkt gestartet wird
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

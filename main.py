import sys
import os
import shutil
from datetime import datetime

from qtpy import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from ui.mainwindow import Ui_MainWindow


import pandas as pd
import csv
from sqlalchemy import create_engine


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,
                 log_source_file_name="",
                 log_query="",
                 log_server_info="",
                 parent=None):
        super().__init__(parent)

        # Erstelle eine Instanz der Benutzeroberfläche aus der generierten Ui-Datei
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("SUN-DOC")

        # query_input-Box verstecken
        self.ui.query_input.hide()
        self.set_log_directories(log_source_file_name=log_source_file_name,
                                 log_query=log_query,
                                 log_server_info=log_server_info)

        # Variablen df und sql_query als Instanzvariable initialisieren
        self.initialize_instance_vars()
        # Verbinde die Signale mit den entsprechenden Slots
        self.map_ui_buttons()
        # Lese die Server-Info aus der Log-Datei
        self.read_server_info_from_log()
        # Lese das zuletzt eingegebene query zur DB-Abfrage
        self.read_query_from_log()
        # setze Tabstops in Eingabefelder ---> funktioniert noch nicht
        self.set_tabstops()

    def map_ui_buttons(self):
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

    def sort_table(self, column, order):
        self.ui.articles_list.sortItems(column, order)

    def initialize_instance_vars(self):
        self.df = None
        self.sql_query = None

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

    def on_source_path_btn_click(self):
        # Öffne einen Dialog für die Auswahl eines Quellordners
        source_path = QFileDialog.getExistingDirectory(
            self, "Select Source Folder")
        if source_path:
            # Setze den ausgewählten Quellordner im Textfeld
            self.ui.source_path_text.setPlainText(source_path)
            # Speichere den Quellordnerpfad in der Log-Datei

            self.write_source_path_to_log(source_path)

    def on_target_path_btn_click(self):
        # Öffne einen Dialog für die Auswahl eines Zielordners
        target_path = QFileDialog.getExistingDirectory(
            self, "Select Target Folder")
        if target_path:
            # Setze den ausgewählten Zielordner im Textfeld
            self.ui.target_path_text.setPlainText(target_path)

    def on_copy_files_btn_click(self):
        # Holen Sie sich Pfade für Quell- und Zielordner aus den Textfeldern
        source_path = self.ui.source_path_text.toPlainText()
        target_path = self.ui.target_path_text.toPlainText()

        # Überprüfe, ob source_path und target_path existieren
        if not os.path.exists(source_path) or not os.path.exists(target_path):
            QtWidgets.QMessageBox.warning(
                self, "Fehler", "Quell- oder Zielpfad existieren nicht.")
            return

        # Holen Sie sich alle Dateinamen im source_path
        source_files = self.get_files_in_source_path(source_path)

        for file in source_files:
            print("--------                " + file)

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

        for file in selected_files:
            print("--------------                " + file)

        # Holen Sie sich alle Dateinamen im Quellordner, die den ausgewählten Dateien entsprechen
        matching_files = []
        matching_files = [file for file in source_files if
                          any(selected_file in file for selected_file in selected_files)]

        for file in matching_files:
            print("-----------------                " + file)

        # Iteriere über alle übereinstimmenden Dateinamen
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
            except Exception as e:
                QtWidgets.QMessageBox.warning(
                    self, "Fehler", f"Fehler beim Kopieren der Datei {source_file_path} zu {target_file_path}.\n\n"
                                    f"Fehler: {e}")

        # Rufen Sie die separate Funktion für das Logging auf
        self.log_copy_details(source_path, target_path,
                              source_files, matching_files)

        # Gib eine Erfolgsmeldung aus
        QtWidgets.QMessageBox.information(self, "Erfolg!",
                                          f"Das Kopieren der Dateien wurde beendet.\n\n"
                                          f"Es wurde eine Logdatei im log-Ordner {self.log_sub2folder_path} erstellt und")

    def fill_article_list(self, file_path=None, df=None):

        # ? Drucke den Dateipfad (optional, zum Testen)
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

    def create_target_directory(self, target_file_path):
        target_directory = os.path.dirname(target_file_path)

        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

    def log_copy_details(self, source_path, target_path, source_files, matching_files):
        # Erstelle einen Zeitstempel für die Log-Datei
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        log_source_file_name = f"datalog_{timestamp}.txt"

        # Erstelle den Unterordner, falls er noch nicht existiert1
        os.makedirs(self.log_subfolder_path, exist_ok=True)
        os.makedirs(self.log_sub2folder_path, exist_ok=True)

        # Pfad zur Log-Datei im Unterordner "logs"
        log_file_path = os.path.join(
            self.log_sub2folder_path, log_source_file_name)

        # Öffne die Log-Datei für das Schreiben
        with open(log_file_path, 'w') as log_file:
            # Schreibe die Quell- und Zielordner in die Log-Datei
            log_file.write(f"Source Folder: {source_path}\n")
            log_file.write(f"Target Folder: {target_path}\n\n")

            # Schreibe alle Dateinamen im source_path in die Log-Datei
            log_file.write("All Files in Source Folder:\n")
            for file in source_files:
                try:
                    log_file.write(f"- {file}\n")
                except Exception as e:
                    QtWidgets.QMessageBox.warning(self, "Fehler!",
                                                  f"Die Datei '{file}' des Quellordners konnte nicht in der log-datei registriert werden.\n\n {e}")
            log_file.write("\n")

            # Schreibe die ausgewählten Artikel in die Log-Datei
            log_file.write("Selected articles:\n")
            for file in matching_files:
                try:
                    log_file.write(f"- {file}\n")
                except Exception as e:
                    QtWidgets.QMessageBox.warning(self, "Fehler!",
                                                  f"Die passende Datei '{file}' des Zielordner konnte nicht in der log-datei registriert werden.\n\n {e}")
            log_file.write("\n")

            # Schreibe das DataFrame in die Log-Datei
            log_file.write("\nDataFrame from File or Database:\n")
            if self.df is not None:
                log_file.write(self.df.to_csv(index=False))

    def on_sql_query_btn_click(self):

        if self.ui.query_input.isHidden():
            self.ui.query_input.show()
        else:
            self.ui.query_input.hide()

    def set_log_directories(self,
                            log_source_file_name,
                            log_query,
                            log_server_info):

        # Setze den dynamischen Pfad zur Log-Datei relativ zum Skript
        if getattr(sys, 'frozen', False):
            # Skript wird im gepackten Zustand ausgeführt
            self.script_dir = os.path.dirname(sys.executable)
        else:
            # Skript wird normal ausgeführt
            self.script_dir = os.path.dirname(os.path.abspath(__file__))
        # Setze den Pfad für die Haupt-Log-Datei
        self.log_file_path = os.path.join(
            self.script_dir, log_source_file_name)
        # Pfad zum Unterordner "logs"
        self.log_subfolder_path = os.path.join(self.script_dir, "logs")
        self.log_sub2folder_path = os.path.join(
            self.log_subfolder_path, "hist")

        # Lese den Quellpfad aus der Log-Datei und setze ihn im Textfeld
        source_path_from_log = self.read_source_path_from_log()

        if source_path_from_log:
            self.ui.source_path_text.setPlainText(source_path_from_log)

        # Setze den Pfad für die query-Log-Datei
        self.query_log_file_path = os.path.join(self.script_dir, log_query)

        # Pfad zur Server-Info-Log-Datei im Unterordner "logs"
        self.server_info_log_path = os.path.join(
            self.script_dir, log_server_info)

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

    def read_sql(self):
        self.sql_query = self.ui.query_input.toPlainText()
        self.write_query_to_log(self.sql_query)
        db_type = self.ui.db_type.currentText()

        # Konfiguriere MySQL-Verbindungsinformationen
        server = self.get_server()  # "127.0.0.1"
        user = self.get_user()  # "root"
        pw = self.get_pw()  # "12345678"
        dB_name = self.get_dB_name()  # "db"

        server_info = f"{server}, {user}, {pw}, {dB_name}"

        # Schreibe die Server-Info in die Log-Datei
        self.write_server_info_to_log(server_info)

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

    def write_source_path_to_log(self, source_path):
        # Schreibe den Quellordnerpfad in die Log-Datei
        os.makedirs(self.log_subfolder_path, exist_ok=True)
        with open(self.log_file_path, 'w') as log_file:
            log_file.write(source_path)

    def read_source_path_from_log(self):
        try:
            # Lese den Quellordnerpfad aus der Log-Datei
            with open(self.log_file_path, 'r') as log_file:
                source_path = log_file.read().strip()
                return source_path
        except FileNotFoundError:
            return None

    def write_query_to_log(self, sql_query):
        # Schreibe den Quellordnerpfad in die Log-Datei
        os.makedirs(self.log_subfolder_path, exist_ok=True)
        with open(self.query_log_file_path, 'w') as query_log_file:
            query_log_file.write(sql_query)

    def read_query_from_log(self):
        try:
            # Lese den Query aus der Log-Datei
            with open(self.query_log_file_path, 'r') as query_log_file:
                self.sql_query = query_log_file.read().strip()
                self.ui.query_input.setPlainText(self.sql_query)
                return self.sql_query
        except FileNotFoundError:
            return None

    def write_server_info_to_log(self, server_info):
        # Erstelle den Unterordner, falls er noch nicht existiert
        os.makedirs(self.log_subfolder_path, exist_ok=True)

        # Schreibe die Server-Info in die CSV-Datei
        with open(self.server_info_log_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([server_info])

    def read_server_info_from_log(self):

        # Versuche, die CSV-Datei zu lesen
        try:
            # Verwende Pandas, um die CSV-Datei mit einer Spalte zu lesen
            df_log = pd.read_csv(self.server_info_log_path,
                                 header=None, names=['ServerInfo'])

            # Überprüfe, ob DataFrame nicht leer ist
            if not df_log.empty:
                # Extrahiere den Wert aus der letzten Zeile der einzigen Spalte
                server_info = df_log.iloc[-1, 0]

                # Rückgabe des Werts
                self.server_info = server_info

        except FileNotFoundError:
            server_info = None
            self.server_info = None

        self.set_server_info_ui_fields(self.server_info)

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

    def set_tabstops(self):
        # Festlegen der Tab-Reihenfolge
        self.setTabOrder(self.ui.project,
                         self.ui.sql_query_btn)

        self.setTabOrder(self.ui.sql_query_btn,
                         self.ui.db_server)

        self.setTabOrder(self.ui.db_server,
                         self.ui.user)

        self.setTabOrder(self.ui.user,
                         self.ui.pw)

        self.setTabOrder(self.ui.pw,
                         self.ui.db_name)

        self.setTabOrder(self.ui.db_name,
                         self.ui.source_path_text)

        self.setTabOrder(self.ui.source_path_text,
                         self.ui.target_path_text)

    def get_project(self):
        # Gibt den Text im Projekt-Textfeld zurück
        return self.ui.project.toPlainText()

    def get_server(self):
        # Gibt den Text im Projekt-Textfeld zurück
        return self.ui.db_server.toPlainText()

    def get_pw(self):
        # Gibt den Text im Projekt-Textfeld zurück
        return self.ui.pw.toPlainText()

    def get_dB_name(self):
        # Gibt den Text im Projekt-Textfeld zurück
        return self.ui.db_name.toPlainText()

    def get_user(self):
        # Gibt den Text im Projekt-Textfeld zurück
        return self.ui.user.toPlainText()


# Führe das Programm aus, wenn es direkt gestartet wird
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(log_source_file_name="logs\\log_source.txt",
                        log_query="logs\\log_query.txt",
                        log_server_info="logs\\log_server_info.csv")
    window.show()
    sys.exit(app.exec_())

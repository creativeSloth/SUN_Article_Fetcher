from cgi import print_directory
import sys
import os
import shutil

from odf.opendocument import load
from odf import text, teletype
from odf.table import Table, TableRow, TableCell

import pandas as pd

from qtpy import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from ui.mainwindow import Ui_MainWindow
from decorators import get_file_path, get_folder_path, check_path_existence
import directory_Handler
import ui_fields_Handler
import logs_and_config
import data_Handler


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

        self.ui.project.textChanged.connect(self.on_project_text_changed)
        self.ui.articles_list.horizontalHeader(
        ).sortIndicatorChanged.connect(self.sort_table)

        #  *********************************** Mapping buttons for "Documentation"- module *****************************************

        self.ui.load_docu_db_data_btn.clicked.connect(
            self.on_load_docu_data_from_db_btn_click)
        self.ui.sql_query_2_btn.clicked.connect(
            self.on_sql_query_2_btn_click)
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
        self.previous_project_text = self.get_project()

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
                df = self.read_data(file_path)
                self.fill_article_list(df=df)

    def on_load_articles_from_db_btn_click(self):
        # Lese Daten aus der MySQL-Datenbank und speichere sie in der Instanzvariable df
        df = data_Handler.execute_query(
            self, data_Handler.get_sql_query(self)['sql1'])
        logs_and_config.update_config_file(self, 'Abfrage', 'sql1',
                                           data_Handler.get_sql_query(self)['sql1'])
        # Lösche die vorhandenen Daten und fülle die Tabelle mit den Daten aus der Datenbank
        self.clear_article_list()
        self.fill_article_list(df=df)

    def on_project_text_changed(self):
        self.char_validation()

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
        df = pd.DataFrame(columns=['article_no', 'article_name'])
        for row in range(self.ui.articles_list.rowCount()):

            checkbox_item = self.ui.articles_list.item(row, 0)
            article_no_item = self.ui.articles_list.item(row, 1)
            article_no = article_no_item.text()
            article_name_item = self.ui.articles_list.item(row, 2)
            article_name = article_name_item.text()

            # Erstelle ein DataFrame mit den neuen Daten
            new_data = pd.DataFrame(
                {'article_no': [article_no], 'article_name': [article_name]})

            # Füge die neuen Daten zum vorhandenen DataFrame hinzu
            df = pd.concat([df, new_data], ignore_index=True)

            # Überprüfe, ob die Checkbox in der aktuellen Zeile angehakt ist
            if checkbox_item and checkbox_item.checkState() == QtCore.Qt.Checked:

                selected_files.append(article_no)

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
                                         source_files, matching_files, df)

        # Gib eine Erfolgsmeldung aus
        QtWidgets.QMessageBox.information(self, "Erfolg!",
                                          f"Das Kopieren der Dateien wurde beendet.\n"
                                          f"Es wurden insgesamt {count} Dateien übertragen.\n\n"
                                          f"Es wurde eine Logdatei im log-Ordner:\n\n {log_sub2folder_path}\n\n erstellt.")

    def fill_article_list(self, df=None):
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

    def get_project(self):
        return self.ui.project.toPlainText()

    def char_validation(self):
        textlength = 10
        # Speichere den vorherigen Text
        prev_string = self.previous_project_text
        current_string = self.get_project()
        cursor = self.ui.project.textCursor()
        cur_cursor_pos = cursor.position()

        # Überprüfe, ob die Länge des aktuellen Strings größer als 10 ist
        if len(current_string) > textlength:
            # Aktuellen Text durch den vorherigen Text ersetzen
            current_string = prev_string
            # Speichere die Position des Cursors vor der Änderung
            prev_cursor_pos = cur_cursor_pos - 1
            # Setze den Text des Textfeldes auf den aktuellen Text
            self.ui.project.setPlainText(current_string)
            # Setze den Cursor wieder auf seine vorherige Position
            cur_cursor_pos = prev_cursor_pos

        # Setze den Cursor auf die vorherige Position
        cursor.setPosition(cur_cursor_pos)

        # Wandle den Text in Großbuchstaben um und aktualisiere den Text im Textfeld
        uppercase_string = self.project_to_uppercase(
            current_string, cur_cursor_pos)

        # Aktualisiere den Textcursor im Textfeld
        self.ui.project.setTextCursor(cursor)

        # Speichere den aktuellen Text als den vorherigen Text
        self.previous_project_text = uppercase_string

    def project_to_uppercase(self, text, cur_cursor_pos):
        if any(char.islower() for char in text):
            # Wandle den Text in Großbuchstaben um
            uppercase_string = "".join(
                char.upper() if char.islower() else char for char in text)
            # Setze den Text des Textfeldes auf den umgewandelten Text
            self.ui.project.setPlainText(uppercase_string)
            cursor = self.ui.project.textCursor()
            cursor.setPosition(cur_cursor_pos)
            return uppercase_string
        else:
            return text

    # Beispiel zum manuellen Einstellen der Spaltenbreite
    def resize_columns_to_contents(self):
        header = self.ui.articles_list.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)


# * * * * * * * * * * * * * * * * * Documentation-module * * * * * * * * * * * * * * * *


    def on_btn_create_docs_clicked(self):
        ui_fields_Handler.set_field_inputs(self)
        self.replace_field()

    def on_load_docu_data_from_db_btn_click(self):
        df = data_Handler.execute_query(
            self, data_Handler.get_sql_query(self)['sql2'])
        logs_and_config.update_config_file(self, 'Abfrage', 'sql2',
                                           data_Handler.get_sql_query(self)['sql2'])
        # self.clear_docu_fields()
        # self.fill_docu_fields(df=df)

    def on_sql_query_2_btn_click(self):
        if self.ui.query_2_input.isHidden():
            self.ui.query_2_input.show()
        else:
            self.ui.query_2_input.hide()

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

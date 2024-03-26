import os
import pandas as pd
from sqlalchemy import create_engine
from qtpy import QtWidgets

import logs_and_config
import ui_fields_Handler


def get_server_info(self):

    server = self.ui.db_server.toPlainText()
    user = self.ui.user.toPlainText()
    password = self.ui.pw.toPlainText()
    dB_name = self.ui.db_name.toPlainText()
    db_type = self.ui.db_type.currentText()
    server_info = {
        'server': server,
        'user': user,
        'password': password,
        'dB_name': dB_name,
        'db_type': db_type
    }
    return server_info


def execute_query(self, query):

    sql_query = get_sql_query(self)[query]

    # Konfiguriere MySQL-Verbindungsinformationen
    server_info = get_server_info(self)
    server = server_info['server']
    user = server_info['user']
    pw = server_info['password']
    dB_name = server_info['dB_name']
    db_type = server_info['db_type']

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
        # if sql_query is None or sql_query == "":
        #     sql_query = "SELECT * FROM articles WHERE project_name = '{{project}}';"
        #     self.ui.query_input.setPlainText(sql_query)
        #     self.ui.query_2_input.setPlainText(sql_query)

        if "{{project}}" in sql_query:
            sql_query = sql_query.replace(
                "{{project}}", ui_fields_Handler.get_project(self))

        # Verwende pd.read_sql, um die Abfrage auszuführen und die Ergebnisse in einen DataFrame zu lesen
        df = pd.read_sql(sql_query, con=engine)
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


def get_sql_query(self):
    sql_query = {'sql1': self.ui.query_input.toPlainText(),

                 'sql2': self.ui.query_2_input.toPlainText()}
    return sql_query


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


def read_csv(file_path):
    # Lese CSV-Datei und gebe DataFrame zurück
    dtypes = {0: str, 1: str}
    df = pd.read_csv(file_path, header=None, dtype=dtypes)
    df = df.drop_duplicates()
    return df


def read_xlsx(file_path):
    # Lese Excel-Datei und gebe DataFrame zurück
    dtypes = {0: str, 1: str}
    df = pd.read_excel(file_path, header=None, dtype=dtypes)
    df = df.drop_duplicates()
    return df


def read_ods(file_path):
    # Lese Excel-Datei und gebe DataFrame zurück
    dtypes = {0: str, 1: str}
    df = pd.read_excel(file_path, header=None, dtype=dtypes, engine="odf")
    df = df.drop_duplicates()
    return df


def read_data_from_file(file_path):
    if file_path.endswith('.csv'):
        return read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return read_xlsx(file_path)
    elif file_path.endswith('.ods'):
        return read_ods(file_path)


def aggr_dev_list(device_list, column_index):
    value = ''
    for row in range(device_list.rowCount()):
        if not device_list.item(row, column_index) == None:
            value = value + device_list.item(row, column_index).text() + '\n'
    value = value.rstrip('\n')
    return value


def get_inv_types(self):

    pass


def get_serial_of_inv(self):
    pass


def get_power_of_inv(self):
    pass

from directories.directory_base import MAIN_PATHS


def init_ui(self):
    # Pfad zur .qss-Datei
    stylesheet_path = MAIN_PATHS.dict["stylesheet_path"]

    # Stylesheet aus der Datei einlesen
    with open(stylesheet_path, "r") as qss_file:
        stylesheet = qss_file.read()

    # Stylesheet auf das Hauptfenster anwenden
    self.setStyleSheet(stylesheet)

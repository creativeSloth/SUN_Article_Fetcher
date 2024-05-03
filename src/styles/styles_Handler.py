from directories.directory_base import get_directories


def initUI(self):
    # Pfad zur .qss-Datei
    stylesheet_path = get_directories(self)['stylesheet_path']

    # Stylesheet aus der Datei einlesen
    with open(stylesheet_path, 'r') as qss_file:
        stylesheet = qss_file.read()

    # Stylesheet auf das Hauptfenster anwenden
    self.setStyleSheet(stylesheet)

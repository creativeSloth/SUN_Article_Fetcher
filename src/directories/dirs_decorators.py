from PyQt5.QtWidgets import QFileDialog


def get_folder_path(func):
    def wrapper(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Wähle den Ordner aus!")
        if folder_path:
            func(self, folder_path)

    return wrapper


def get_file_path(func):
    def wrapper(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Wähle die Datei aus!")
        if file_path:
            func(self, file_path)

    return wrapper

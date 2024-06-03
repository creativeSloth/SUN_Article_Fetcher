import subprocess
import os
import shutil

# Hilfsfunktion, um das Wurzelverzeichnis zu ermitteln


def get_root_directory(path):
    parts = path.split(os.sep)
    return parts[0] if parts else ""


# Initialisiere die Liste zum Speichern der Quell- und Zielpfade
items = []
file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(file_path)
SOURCE_DIR = r"R:\_Projektrealisierung\_Dokumente\Doku\SUN DocFetcher\PyProjekt\SUN_Article_Fetcher-main\src\main.py"

# Pfad zur Textdatei
paths_dir = os.path.join(BASE_DIR, 'paths.txt')

# Pfade aus der Textdatei lesen
with open(paths_dir, 'r') as file:
    data_paths = file.readlines()

# PyInstaller-Befehl aufbauen
pyinstaller_command = [
    'pyinstaller',
    '--windowed',
    '--distpath', BASE_DIR
]

# Füge jedes --add-data Argument hinzu
for path in data_paths:
    path = path.strip()  # Entferne Leerzeichen und Zeilenumbrüche
    src, dest_folder = path.split(';')

    dest_dir = os.path.join(BASE_DIR, 'main')
    src_dir = os.path.join(BASE_DIR, 'main', '_internal', dest_folder)
    pyinstaller_command.extend(['--add-data',
                                f'{src}{os.pathsep}{dest_folder}'])

    # Bestimme das Wurzelverzeichnis des Zielordners
    src_dir_root = os.path.join(BASE_DIR, 'main', '_internal',
                                get_root_directory(dest_folder))
    dest_dir_root = os.path.join(BASE_DIR, 'main',
                                 get_root_directory(dest_folder))
    items.append((src_dir_root, dest_dir_root))

# Füge die Hauptdatei hinzu
pyinstaller_command.append(SOURCE_DIR)

# Führe den PyInstaller-Befehl aus
subprocess.run(pyinstaller_command)

# Verschiebe die angegebenen Verzeichnisse nach dem Ausführen von PyInstaller
for src_dir_root, dest_dir_root in items:
    src_dir_root = os.path.abspath(src_dir_root)
    dest_dir = os.path.abspath(dest_dir_root)

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    if os.path.exists(src_dir_root):
        for item_name in os.listdir(src_dir_root):
            shutil.move(os.path.join(src_dir_root, item_name), dest_dir)

    # Entferne das leere Quellverzeichnis
    if os.path.exists(src_dir_root):
        shutil.rmtree(src_dir_root)

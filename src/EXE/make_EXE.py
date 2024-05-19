import subprocess
import os
import shutil


items = []
file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(file_path)
SOURCE_DIR = "D:/3441\Documents\Familie\Edgar\Weiterbildungen\Kurse\Python Bootcamp\Projekte\SUN_Article_Fetcher\src\main.py"


paths_dir = os.path.join(BASE_DIR, 'paths.txt')
# print("paths_dir: " + paths_dir)

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
    src_dir = os.path.join(BASE_DIR, 'main', '_internal',
                           dest_folder)

    items.append((src_dir, dest_dir))
    pyinstaller_command.extend(['--add-data', f'{path}'])

# Füge die Hauptdatei hinzu
pyinstaller_command.append(SOURCE_DIR)

# Führe den PyInstaller-Befehl aus
subprocess.run(pyinstaller_command)

for item in items:
    src_dir = os.path.abspath(item[0])
    dest_dir = os.path.abspath(item[1])

    os.makedirs(dest_dir, exist_ok=True)
    shutil.move(src_dir, dest_dir)

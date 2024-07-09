import inspect
import os
import sys

from directories.constants import dir_paths


def get_main_dir() -> str:
    # Finde das Verzeichnis, in dem main.py liegt
    main_script_path = inspect.getsourcefile(sys.modules["__main__"])
    main_script_dir = os.path.dirname(main_script_path)

    # Setze den dynamischen Pfad zur Log-Datei relativ zum Verzeichnis von main.py
    if getattr(sys, "frozen", False):
        # Skript wird im gepackten Zustand ausgeführt
        script_dir = os.path.dirname(sys.executable)
    else:
        # Skript wird normal ausgeführt
        script_dir = main_script_dir

    return script_dir


def create_storage_files(log_path):
    script_dir = get_main_dir()
    # Pfad zur Config
    config_path = os.path.join(log_path, "config.ini")
    # Pfad zur blacklist
    blacklist_path = os.path.join(log_path, "blacklist.ini")
    blacklist_db_path = os.path.join(log_path, "blacklist.db")
    device_specs_list_path = os.path.join(log_path, "device_specs_list.ini")
    stylesheet_path = os.path.join(script_dir, "styles", "stylesheet.qss")
    icons_folder_path = os.path.join(script_dir, "ui", "icons")
    return (
        config_path,
        blacklist_path,
        blacklist_db_path,
        device_specs_list_path,
        stylesheet_path,
        icons_folder_path,
    )


def create_static_dirs():
    log_subfolder_path, log_subfolder_2_path = create_log_subfolders()
    (
        config_path,
        blacklist_path,
        blacklist_db_path,
        device_specs_list_path,
        stylesheet_path,
        icons_folder_path,
    ) = create_storage_files(log_subfolder_path)
    return (
        log_subfolder_path,
        log_subfolder_2_path,
        config_path,
        blacklist_path,
        blacklist_db_path,
        device_specs_list_path,
        stylesheet_path,
        icons_folder_path,
    )


def create_log_subfolders():
    script_dir = get_main_dir()
    # Pfad zum Unterordner "logs"
    log_subfolder_path = os.path.join(script_dir, "logs")
    os.makedirs(log_subfolder_path, exist_ok=True)
    log_subfolder_2_path = os.path.join(log_subfolder_path, "hist")
    os.makedirs(log_subfolder_2_path, exist_ok=True)
    return log_subfolder_path, log_subfolder_2_path


def set_static_directories():

    (
        log_subfolder_path,
        log_subfolder_2_path,
        config_path,
        blacklist_path,
        blacklist_db_path,
        device_specs_list_path,
        stylesheet_path,
        icons_folder_path,
    ) = create_static_dirs()

    # Setze die Pfade direkt im dict-Attribut der _main_paths Instanz
    dir_paths.set_path("log_subfolder_path", log_subfolder_path)
    dir_paths.set_path("log_subfolder_2_path", log_subfolder_2_path)
    dir_paths.set_path("config_path", config_path)
    dir_paths.set_path("blacklist_path", blacklist_path)
    dir_paths.set_path("blacklist_db_path", blacklist_db_path)
    dir_paths.set_path("device_specs_list_path", device_specs_list_path)
    dir_paths.set_path("stylesheet_path", stylesheet_path)
    dir_paths.set_path("icons_folder_path", icons_folder_path)

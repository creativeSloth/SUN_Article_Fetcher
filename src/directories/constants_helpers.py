import inspect
import os
import sys

from directories.constants import (
    BLACKLISTS_NAME,
    CONFIG,
    CONFIG_NAME,
    DB,
    DB_NAME,
    DEVICE_SPECS_NAME,
    DIRS,
    ICONS_FOLDER,
    ICONSF_NAME,
    ICONSSUPERF_NAME,
    LOG_SUBF,
    LOG_SUBF_2,
    LOG_SUBF_2_NAME,
    LOG_SUBF_NAME,
    STYLESHEET,
    STYLESHEET_NAME,
    STYLESHEETF_NAME,
)


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
    config_path = os.path.join(log_path, CONFIG_NAME)
    # Pfad zur blacklist
    # blacklist_path = os.path.join(log_path, BLACKLISTS_NAME)
    db_path = os.path.join(log_path, DB_NAME)
    # device_specs_list_path = os.path.join(log_path, DEVICE_SPECS_NAME)
    stylesheet_path = os.path.join(script_dir, STYLESHEETF_NAME, STYLESHEET_NAME)
    icons_folder_path = os.path.join(script_dir, ICONSSUPERF_NAME, ICONSF_NAME)
    return (
        config_path,
        # blacklist_path,
        db_path,
        # device_specs_list_path,
        stylesheet_path,
        icons_folder_path,
    )


def create_static_dirs():
    log_subfolder_path, log_subfolder_2_path = create_log_subfolders()
    (
        config_path,
        # blacklist_path,
        db_path,
        # device_specs_list_path,
        stylesheet_path,
        icons_folder_path,
    ) = create_storage_files(log_subfolder_path)
    return (
        log_subfolder_path,
        log_subfolder_2_path,
        config_path,
        # blacklist_path,
        db_path,
        # device_specs_list_path,
        stylesheet_path,
        icons_folder_path,
    )


def create_log_subfolders():
    script_dir = get_main_dir()
    # Pfad zum Unterordner "logs"
    log_subfolder_path = os.path.join(script_dir, LOG_SUBF_NAME)
    os.makedirs(log_subfolder_path, exist_ok=True)
    log_subfolder_2_path = os.path.join(log_subfolder_path, LOG_SUBF_2_NAME)
    os.makedirs(log_subfolder_2_path, exist_ok=True)
    return log_subfolder_path, log_subfolder_2_path


def set_static_directories():

    (
        log_subfolder_path,
        log_subfolder_2_path,
        config_path,
        # blacklist_path,
        db_path,
        # device_specs_list_path,
        stylesheet_path,
        icons_folder_path,
    ) = create_static_dirs()

    # Setze die Pfade direkt im dict-Attribut der _main_paths Instanz
    DIRS.set_path(LOG_SUBF, log_subfolder_path)
    DIRS.set_path(LOG_SUBF_2, log_subfolder_2_path)
    DIRS.set_path(CONFIG, config_path)
    # dir_paths.set_path("blacklist_path", blacklist_path)
    DIRS.set_path(DB, db_path)
    # DIRS.set_path(DEVICE_SPECS, device_specs_list_path)
    DIRS.set_path(STYLESHEET, stylesheet_path)
    DIRS.set_path(ICONS_FOLDER, icons_folder_path)

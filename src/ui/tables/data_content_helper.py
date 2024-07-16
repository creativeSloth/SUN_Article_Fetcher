import os
from typing import List

from pandas import DataFrame, Series
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget

from database.constants import COLUMN_ARTICLE_NO
from database.queries import (
    get_bl_df_from_db,
    get_value_from_db_art_specs_list,
    update_db_article_spec_list,
)

# from directories.constants import BLACKLISTS, BLACKLISTS_NAME, DIRS
from files.sys_files import get_files_in_directory, get_paths

# from ui.blacklists.storage_file import transmit_bl_from_file_to_db
from ui.blacklists.storage_file_utils import get_article_numbers_on_bl
from ui.buttons.button_lists import add_btns_into_table_cells, add_doc_avlbl_btns
from ui.tables.utils import (
    clear_table,
    get_column_index,
    get_fixed_val_columns,
    import_from_df_row,
    is_on_bl,
    remove_article_from_table_row,
)
from ui.text_edits.ui_fields_base import get_articles_table, get_device_tables

# from files.logs_and_config import update_device_related_storage_list


def put_non_bl_articles_on_table_via_db(
    self,
    table: QtWidgets.QTableWidget,
    all_articles_df: DataFrame,
    import_column_count: int = 0,
) -> None:
    """
    Sammelt nicht-Blacklistige Artikel aus dem DataFrame und fügt sie in die angegebene Tabelle ein.
    ________________________________________________________________________________________________________________________________
    :param table: QTableWidget, in der die Artikel eingefügt werden sollen
    :param all_articles_df : DataFrame, aus dem die Artikel geladen werden sollen
    :param import_column_count: Anzahl der Spalten, die von der Datenbank importiert werden sollen
    :return: None
    ________________________________________________________________________________________________________________________________
    """
    if all_articles_df is None:
        return

    clear_table(table=table)

    bl_df: DataFrame = get_bl_df_from_db(self, table)
    if bl_df is None:
        return

    blacklist_article_numbers: set = set(bl_df[COLUMN_ARTICLE_NO])

    # #! ________________________________________________________________________________________________________________________________

    # #! Der folgende Abschnitt kann entfernt werden, wenn alte blacklists.ini erfolgreich in db.blacklists übertragen wurde
    # if os.path.exists(DIRS.paths[BLACKLISTS]):
    #     transmit_bl_from_file_to_db(self, table)
    #     # print(f"Die Datei '{BLACKLISTS_NAME}' existiert!")
    # # else:
    # # print(f"Die Datei '{BLACKLISTS_NAME}' existiert nicht!")

    # #! ________________________________________________________________________________________________________________________________

    count: int = 0
    for _, df_row in all_articles_df.iterrows():

        # Überprüfen Sie, ob die Artikelnummer nicht in der Blacklist enthalten ist
        if is_on_bl(blacklist_article_numbers=blacklist_article_numbers, df_row=df_row):
            continue
        import_from_df_row(
            table, data_row=df_row, import_column_count=import_column_count
        )

        if table in get_articles_table(self):
            mark_documents_availability(self, table, row=count)

        add_btns_into_table_cells(
            self,
            table,
            row=count,
            column=table.columnCount() - 1,
            button_type="move_to_bl",
            on_button_pressed=remove_article_from_table_row,
        )
        count += 1


def collect_table_data(
    table, article_no_col_index: int, discard_columns: List[str]
) -> set:
    """Sammle Artikelspezifikationen aus der Tabelle
    ________________________________________________________________________________________________________________________________
    :param table: QTableWidget, aus der die Artikelspezifikationen geladen werden sollen
    :param article_no_col_index: int, die Spaltennummer der Artikelnummer in der Tabelle
    :param discard_columns: Liste der Spalten, die nicht in den Artikelspezifikationen geladen werden sollen
    :return: Set mit allen verfügbaren Artikelspezifikationen
    ________________________________________________________________________________________________________________________________
    """
    data_set = set()

    for row in range(table.rowCount()):
        article_no = table.item(row, article_no_col_index)
        if article_no is None:
            return

        article_no = article_no.text()
        article_name = table.item(row, article_no_col_index + 1).text()
        for column in range(5, table.columnCount()):

            column_header = table.horizontalHeaderItem(column).text()
            if column_header in discard_columns:
                continue

            spec_item = table.horizontalHeaderItem(column)
            if spec_item is None:
                continue

            value_item = table.item(row, column)
            if value_item is None:
                continue

            spec = spec_item.text()
            value = value_item.text()  # if value_item.text() is not None else ""

            data_set.add((article_no, article_name, spec, value))
    return data_set


def collect_specs_of_articles(self):

    device_tables = get_device_tables(self)
    fixed_val_columns = get_fixed_val_columns()

    data_set = set()
    for table in device_tables:
        # Suche den Index der 'Artikelnummer'-Spalte in einer der Tabellen

        article_no_col_index = get_column_index(table, "Artikelnummer")

        # Beende die Funktion, wenn die 'Artikelnummer'-Spalte nicht gefunden wurde
        if article_no_col_index is None:
            continue

        data_set |= collect_table_data(table, article_no_col_index, fixed_val_columns)

    # Sortiere das data_set nach der section
    # sorted_data_set = sorted(data_set, key=lambda x: x[0])

    # Aktualisiere die Gerätespezifikationsliste
    update_db_article_spec_list(data_set)
    # update_device_related_storage_list("device_specs_list_path", sorted_data_set)


def fill_device_specs_in_device_tables(table: QTableWidget) -> None:
    """
    Füllt die Geräteeigenschaften aus den in der Datenbank hinterlegten Werten in die entsprechende Zelle des QTableWidgets.

    ________________________________________________________________________________________________________________________________
    :param table: QTableWidget, in der die Gerätespezifikationen geladen werden sollen
    :return: None
    ________________________________________________________________________________________________________________________________
    """

    fixed_val_columns = get_fixed_val_columns()

    # Finde Spaltenindex der Artikelnummer
    article_no_col_index = get_column_index(table, "Artikelnummer")

    for row in range(table.rowCount()):
        for column in range(5, table.columnCount()):
            column_header = table.horizontalHeaderItem(column).text()
            if column_header in fixed_val_columns:
                continue
            article_no_item = table.item(row, article_no_col_index)
            if article_no_item:
                article_no = article_no_item.text()

                article_no = table.item(row, article_no_col_index).text()
                # value = logs_and_config.read_device_related_storage_list(
                #     "device_specs_list_path", article_no, column_header
                # )
                value = get_value_from_db_art_specs_list(
                    article_no=article_no, column_header=column_header
                )
                if value is None:
                    continue
                table.setItem(row, column, QtWidgets.QTableWidgetItem(value))


def mark_documents_availability(self, table: QTableWidget = None, row: int = 0) -> None:
    """
    Fügt einen Knopf in die 1. Spalte von links des angegebenen QTableWidget
    ________________________________________________________________________________________________________________________________
    :param table: QTableWidget
    :return: None
    ________________________________________________________________________________________________________________________________
    """

    source_path, _, _ = get_paths()
    all_files: list[str] = get_files_in_directory(self, directory=source_path)
    add_doc_avlbl_btns(
        self,
        table=table,
        column=0,
        button_type="doc_available",
        all_files=all_files,
        on_button_pressed=None,
        row=row,
    )


def put_non_bl_articles_on_table_via_file(
    table: QtWidgets.QTableWidget, df: DataFrame, import_column_count: int = 0
):
    """
    Sammelt nicht-Blacklistige Artikel aus dem DataFrame und fügt sie in die angegebene Tabelle ein.
    :param table: QTableWidget, in der die Artikel eingefügt werden sollen
    :param df: DataFrame, aus dem die Artikel geladen werden sollen
    :param import_column_count: Anzahl der Spalten, die von der Datenbank importiert werden sollen
    :return: None"""
    clear_table(table=table)

    blacklist_article_numbers = get_article_numbers_on_bl(table)

    if df is not None:
        for _, df_row in df.iterrows():
            # Überprüfen Sie, ob die Artikelnummer nicht in der Blacklist enthalten ist
            if is_on_bl(
                blacklist_article_numbers=blacklist_article_numbers, df_row=df_row
            ):
                continue
            import_from_df_row(
                table, data_row=df_row, import_column_count=import_column_count
            )

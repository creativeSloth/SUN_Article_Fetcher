from typing import List

from pandas import DataFrame
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget

from database.constants import COLUMN_ARTICLE_NAME, COLUMN_ARTICLE_NO
from database.queries import (
    get_bl_df_from_db,
    get_value_from_db_art_specs_list,
    update_db_article_spec_list,
)
from files.sys_files import get_files_in_directory, get_paths
from ui.blacklists.gui_window import BlacklistWindow
from ui.buttons.button_lists import add_doc_avlbl_btns
from ui.tables.decorators import customize_table_row
from ui.tables.utils import (
    clear_table,
    get_column_index,
    get_fixed_val_columns,
    import_from_df_row,
    is_on_bl,
)
from ui.text_edits.ui_fields_base import get_device_tables


@customize_table_row
def none_bl_art_to_table(
    self,
    table: QtWidgets.QTableWidget,
    df: DataFrame,
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
    if df is None:
        return

    clear_table(table=table)
    table.verticalScrollBar().setValue(0)

    bl_df: DataFrame = get_bl_df_from_db(self, table)
    if bl_df is None:
        return

    blacklist_article_numbers: set = set(bl_df[COLUMN_ARTICLE_NO])

    for _, df_row in df.iterrows():

        # Überprüfen Sie, ob die Artikelnummer nicht in der Blacklist enthalten ist
        if is_on_bl(blacklist_article_numbers=blacklist_article_numbers, df_row=df_row):
            continue
        import_from_df_row(
            table, data_row=df_row, import_column_count=import_column_count
        )


def bl_art_to_bl(self, bl_table: QTableWidget) -> None:
    """
    Öffnet eine neue Blacklist und fügt alle Artikelnummern aus der angegebenen Blacklist-Tabelle hinzu
    ________________________________________________________________________________________________________________________________
    :param bl_table: QTableWidget, in der die Blacklist-Artikel hinzugefügt werden sollen
    :return: None
    ________________________________________________________________________________________________________________________________
    """
    dialog_instance: BlacklistWindow = getattr(bl_table, "related_window", None)
    if dialog_instance is None:
        return
    else:
        dialog_instance.show()

    clear_table(table=bl_table)
    bl_table.verticalScrollBar().setValue(0)

    related_table = getattr(bl_table, "related_table", None)
    bl_df = get_bl_df_from_db(self, table=related_table)
    bl_df_selected: DataFrame = bl_df[
        [
            COLUMN_ARTICLE_NO,
            COLUMN_ARTICLE_NAME,
            self.GENERAL_TABLE_MAP[related_table]["db_added_to_bl_date"],
        ]
    ]

    # Zum Sicherstellen dass bl_articles eine Instanz von List ist und ein Element hat
    if isinstance(bl_df_selected, DataFrame):
        # Füge jede Zeile der Blacklist-Tabelle hinzu, um die Daten der Artikel zu importieren
        from ui.tables.utils import import_from_df_row

        for _, data in bl_df_selected.iterrows():
            # Import data from each row of the blacklist articles
            import_from_df_row(bl_table, data_row=data, import_column_count=3)


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

    # Aktualisiere die Gerätespezifikationsliste
    update_db_article_spec_list(data_set)


def dev_specs_to_table(table: QTableWidget) -> None:
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

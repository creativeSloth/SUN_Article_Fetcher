from typing import Any

from PyQt5.QtWidgets import QDialog, QPushButton, QTableWidget

from database.queries import update_db_blacklist
from styles.styles_Handler import initialize_ui_style
from ui.blacklists.constants import BLACKLISTS, BLACKLISTS_TABLE_MAP
from ui.blacklists.storage_file import remove_articles_from_bl
from ui.buttons.button_lists import add_btns_into_table_cells
from ui.buttons.custom_button import customize_push_buttons
from ui.tables.utils import (
    clear_table,
    disable_colums_edit,
    remove_row_with_button_from_table,
    resize_columns_to_contents,
)
from ui.windows import blacklistWindow


class BlacklistWindow(QDialog):

    def __init__(
        self,
        related_table: QTableWidget = None,
        table_name: str = "",
        table_name_ger: str = "",
        parent: Any = None,
    ):
        super().__init__(parent)
        self.ui = blacklistWindow.Ui_blacklist_dialog()
        self.ui.setupUi(self)
        self.related_table: QTableWidget = related_table
        setattr(self.ui.blacklist, "related_table", self.related_table)
        self.table_name: str = table_name
        self.table_name_ger: str = table_name_ger

        self.setWindowTitle(table_name_ger)

        self.initialize()

    def initialize(self):
        initialize_ui_style(self)

        from ui.tables.utils import connect_sort_indicator_changed

        connect_sort_indicator_changed(self)


def initialize_blacklist_dialogs(self):
    tables_dict = self.GENERAL_TABLE_MAP

    for key, value in tables_dict.items():
        table: QTableWidget
        table_name_ger: str

        table, table_name_ger = key, value["name_translated_german"]
        table_name_ger = f"{table_name_ger} - Blacklist"

        table_name = table.objectName()

        # Erstelle dynamisch ein Attribut für jede Tabelle
        setattr(
            self,
            f"{table_name}_blacklist_dlg",
            BlacklistWindow(
                related_table=table,
                table_name=table_name,
                table_name_ger=table_name_ger,
                parent=self,
            ),
        )

        dialog_instance: BlacklistWindow = getattr(
            self, f"{table_name}_blacklist_dlg", None
        )

        dialog_instance.setObjectName(f"{table_name}")

        BLACKLISTS_TABLE_MAP.append(
            (dialog_instance.ui.blacklist, dialog_instance.ui.verticalLayout)
        )
        BLACKLISTS.append(dialog_instance)


def init_blacklist_button_click_signal(self, table: QTableWidget):

    button = self.GENERAL_TABLE_MAP[table]["gui_open_bl_btn"]
    if button:
        button.clicked.connect(
            lambda: on_blacklist_button_click(self, device_table=table)
        )

    # fill_bl_tables(self, device_table=device_table, table=blacklist_table)
    # add_btns_into_table_cells(
    #     dialog_instance,
    #     table=blacklist_table,
    #     column=4,
    #     button_type="move_from_bl",
    #     on_button_pressed=on_remove_articles_from_gui_bl,
    # )


def on_remove_articles_from_gui_bl(
    self,
    bl_table: QTableWidget = None,
    push_button: QPushButton = None,
):
    related_table = getattr(bl_table, "related_table", None)
    removed, article_no, article_name = remove_row_with_button_from_table(
        table=bl_table, push_button=push_button
    )
    if removed:
        # remove_articles_from_bl(related_table=related_table, article_no=article_no)
        update_db_blacklist(
            self.parent(),
            article_no=article_no,
            article_name=article_name,
            table=related_table,
            mode="remove",
        )


def on_blacklist_button_click(self, device_table: QTableWidget) -> None:
    # device_table_name: str = device_table.objectName()

    # # Zugriff auf die entsprechende Instanz des Blacklist-Dialogs
    # dialog_instance: BlacklistWindow = getattr(
    #     self, f"{device_table_name}_blacklist_dlg", None
    # )
    # blacklist_table: QTableWidget = dialog_instance.ui.blacklist
    # # Überprüfe, ob die Instanz existiert, bevor du die Methode aufrufst
    # if dialog_instance is not None:
    #     dialog_instance.show()
    # clear_table(blacklist_table)
    from ui.tables.data_content import fill_bl_tables

    fill_bl_tables(self, table=device_table)

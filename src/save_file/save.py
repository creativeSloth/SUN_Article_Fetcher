import files.logs_and_config as logs_and_config
from ui.fields.ui_fields_base import get_all_tables, get_mapped_context


def save_fields_text(self, file_path):

    mapped_values = get_mapped_context(self).values()
    field_map = [
        (field[0].objectName(), field[0].toPlainText()) for field in mapped_values
    ]
    logs_and_config.update_save_file(
        field_map=field_map, file_path=file_path, section="Fields text"
    )


def save_tables_content(self, file_path):
    tables = get_all_tables(self)
    field_map = []
    for table in tables:
        for row in range(table.rowCount()):

            for column in range(table.columnCount()):
                if column == 0:
                    continue
                value = table.item(row, column).text()

                table_map = f"{table.objectName()}({row};{column})"
                field_map.append((table_map, value))

    logs_and_config.update_save_file(
        field_map=field_map, file_path=file_path, section="Tables content"
    )

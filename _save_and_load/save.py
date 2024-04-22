import logs_and_config
import _ui_fields_Handler.ui_fields


def save_fields_text(self, file_path):

    mapped_values = _ui_fields_Handler.ui_fields.get_mapped_context(
        self).values()
    field_map = [(field[0].objectName(), field[0].toPlainText())
                 for field in mapped_values]
    logs_and_config.update_save_file(
        field_map=field_map, file_path=file_path, section='Fields text')


def save_tables_content(self, file_path):
    tables = _ui_fields_Handler.ui_fields.get_all_tables(self)
    field_map = []
    for table in tables:
        for row in range(table.rowCount()):

            for column in range(table.columnCount()):
                if column == 0:
                    continue
                value = table.item(row, column).text()

                table_map = f'{table.objectName()}({row};{column})'
                field_map.append((table_map, value))

    logs_and_config.update_save_file(
        field_map=field_map, file_path=file_path, section='Tables content')

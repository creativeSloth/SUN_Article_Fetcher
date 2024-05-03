import files.logs_and_config as logs_and_config
import ui_fields.ui_fields_base


def save_fields_text(self, file_path):

    mapped_values = ui_fields.ui_fields_base.get_mapped_context(
        self).values()
    field_map = [(field[0].objectName(), field[0].toPlainText())
                 for field in mapped_values]
    logs_and_config.update_save_file(
        field_map=field_map, file_path=file_path, section='Fields text')


def save_tables_content(self, file_path):
    tables = ui_fields.ui_fields_base.get_all_tables(self)
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

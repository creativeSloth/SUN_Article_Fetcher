import logs_and_config
from _tables.interactions import fill_tables_content
import _ui_fields_Handler.ui_fields


def load_fields_text(self, file_path):
    section = 'Fields text'

    field_map = _ui_fields_Handler.ui_fields.get_mapped_context(self)
    saved_field_texts = logs_and_config.load_save_file(
        file_path, section)
    for _, field in field_map.items():
        fill_field_value(field[0], saved_field_texts)


def fill_field_value(field, saved_field_texts):
    field_name = field.objectName().lower()

    if field_name in saved_field_texts:
        field.setPlainText(saved_field_texts[field_name])


def load_tables_content(self, file_path):
    section = 'Tables content'

    saved_tables_content = logs_and_config.load_save_file(
        file_path, section)

    fill_tables_content(self, saved_tables_content)

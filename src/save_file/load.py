import files.logs_and_config as logs_and_config
from ui.fields.ui_fields_base import get_mapped_context
from ui.tables.tables_base import fill_tables_content


def load_fields_text(self, file_path):
    section = "Fields text"

    field_map = get_mapped_context(self)
    saved_field_texts = logs_and_config.load_save_file(file_path, section)
    for _, field in field_map.items():
        fill_field_value(field[0], saved_field_texts)


def fill_field_value(field, saved_field_texts):
    field_name = field.objectName().lower()

    if field_name in saved_field_texts:
        field.setPlainText(saved_field_texts[field_name])


def load_tables_content(self, file_path):
    section = "Tables content"

    saved_tables_content = logs_and_config.load_save_file(file_path, section)

    fill_tables_content(self, saved_tables_content)

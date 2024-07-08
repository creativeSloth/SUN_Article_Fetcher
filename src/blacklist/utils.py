def is_on_blacklist(table_name, art_no, config):
    return config.has_section(table_name) and config.has_option(table_name, art_no)

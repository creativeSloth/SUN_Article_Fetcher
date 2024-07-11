from ui.blacklists.constants import COLUMN_ARTICLE_NAME, COLUMN_ARTICLE_NO


def get_query_for_articles_on_table(self, db_table, bool_arg, date_arg):
    bl_bool_article_list = self.GENERAL_TABLE_MAP[self.ui.articles_list]["db_bl_bool"]

    return f"""
    SELECT 
        {COLUMN_ARTICLE_NAME},
        {COLUMN_ARTICLE_NO},
        {bool_arg},
        {date_arg}
    FROM 
        {db_table}
    WHERE
        {bool_arg} = TRUE 
    OR    
        {bl_bool_article_list} = TRUE
    """

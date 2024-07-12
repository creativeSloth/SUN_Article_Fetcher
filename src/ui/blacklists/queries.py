from ui.blacklists.constants import (
    COLUMN_ARTICLE_NAME,
    COLUMN_ARTICLE_NO,
    DB_TABLE_NAME_ARTICLES,
    DB_TABLE_NAME_BLACKLISTS,
)


def get_query_for_articles_on_table(self, db_table, bool_arg, date_arg):
    bl_bool_article_list = self.GENERAL_TABLE_MAP[self.ui.articles_list]["db_bl_bool"]

    return f"""
    SELECT 
        {DB_TABLE_NAME_ARTICLES}.{COLUMN_ARTICLE_NAME},
        {DB_TABLE_NAME_ARTICLES}.{COLUMN_ARTICLE_NO},
        {DB_TABLE_NAME_BLACKLISTS}.{bool_arg},
        {DB_TABLE_NAME_BLACKLISTS}.{date_arg}
    FROM 
        {DB_TABLE_NAME_ARTICLES}
    INNER JOIN 
        {DB_TABLE_NAME_BLACKLISTS} 
    ON 
        {DB_TABLE_NAME_ARTICLES}.id = {DB_TABLE_NAME_BLACKLISTS}.article_id
    WHERE
        {DB_TABLE_NAME_BLACKLISTS}.{bool_arg} = TRUE 
    OR    
        {DB_TABLE_NAME_BLACKLISTS}.{bl_bool_article_list} = TRUE
    """

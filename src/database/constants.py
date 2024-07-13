from sqlalchemy.ext.declarative import declarative_base

COLUMN_ARTICLE_NO = "article_no"
COLUMN_ARTICLE_NAME = "article_name"
DB_TABLE_NAME_ARTICLES = "articles"
DB_TABLE_NAME_BLACKLISTS = "blacklists"
DB_TABLE_NAME_ART_SPECS = "art_specs"
BASE = declarative_base()

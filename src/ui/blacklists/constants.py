from typing import List

from sqlalchemy.ext.declarative import declarative_base

COLUMN_ARTICLE_NO = "article_no"
COLUMN_ARTICLE_NAME = "article_name"
DB_TABLE_NAME_BLACKLISTS = "blacklists"
BLACKLISTS: List = []
BLACKLISTS_TABLE_MAP: List = []

BASE = declarative_base()

from typing import List

from sqlalchemy.ext.declarative import declarative_base

BLACKLISTS: List = []
BLACKLISTS_TABLE_MAP: List = []

BASE = declarative_base()

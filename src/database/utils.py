from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from directories.constants import DB, DIRS


def set_val_by_mode(mode):
    if mode == "add":
        bl_bool_val: bool = True
        bl_date_val: str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    elif mode == "remove":
        bl_bool_val: bool = False
        bl_date_val: str = None

    return bl_bool_val, bl_date_val


def get_db_engine():
    db_path: str = DIRS.paths[DB]
    engine = create_engine(f"sqlite:///{db_path}", echo=False)
    return engine


def create_session():
    ENGINE = get_db_engine()
    Session = sessionmaker(bind=ENGINE)
    session = Session()

    return session

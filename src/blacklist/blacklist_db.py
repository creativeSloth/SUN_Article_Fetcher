from sqlalchemy import Boolean, Column, Date, Engine, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from directories.constants import dir_paths

# Erstelle eine SQLite-Datenbank in Pfad


Base = declarative_base()


# Definition der Tabelle
class Blacklists(Base):
    __tablename__ = "blacklists"

    id = Column(Integer, primary_key=True, autoincrement=True)
    article_no = Column(String, nullable=False, unique=True)
    article_name = Column(String, nullable=False)

    on_articles_blacklist = Column(Boolean, default=False)
    on_modules_blacklist = Column(Boolean, default=False)
    on_pv_inv_blacklist = Column(Boolean, default=False)
    on_bat_inv_blacklist = Column(Boolean, default=False)
    on_bat_blacklist = Column(Boolean, default=False)
    on_chg_point_blacklist = Column(Boolean, default=False)

    added_to_articles_bl = Column(Date, nullable=True)
    added_to_modules_blacklist = Column(Date, nullable=True)
    added_to_pv_inv_blacklist = Column(Date, nullable=True)
    added_to_bat_inv_blacklist = Column(Date, nullable=True)
    added_to_bat_blacklist = Column(Date, nullable=True)
    added_to_chg_point_blacklist = Column(Date, nullable=True)


def init_blacklists_db(self):
    db_path: str = dir_paths.dict["blacklist_db_path"]
    self.engine = create_engine(f"sqlite:///{db_path}", echo=True)
    Base.metadata.create_all(self.engine)


def add_bl_article_to_db(self, article_no, article_name, blacklist):
    Session = sessionmaker(bind=self.engine)

    with Session() as session:
        new_blacklist_entry = Blacklists(
            article_no=article_no, article_name=article_name, **blacklist
        )
        session.add(new_blacklist_entry)
        session.commit()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base


class Database:
    def __init__(self, db_url='sqlite:///investor.db', echo=False):
        self.engine = create_engine(db_url, echo=echo)
        self.Session = sessionmaker(bind=self.engine)

    def init_db(self):
        Base.metadata.drop_all(bind=self.engine)
        Base.metadata.create_all(self.engine)

from sqlalchemy import create_engine, Engine, inspect
from sqlalchemy.orm import sessionmaker

from backend.app.orm_models import Base


sync_engine = create_engine('sqlite:///database.db')


class DBHelper:
    def __init__(self, engine: Engine = sync_engine):
        self.engine = engine
        self.inspector = inspect(self.engine)
        self.Session = sessionmaker(bind=engine)

    def drop_tables(self):
        Base.metadata.drop_all(self.engine)

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def has_tables(self):
        return bool(self.inspector.get_table_names())


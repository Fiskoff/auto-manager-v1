from sqlalchemy import create_engine, Engine, inspect, Inspector
from sqlalchemy.orm import sessionmaker

from backend import Base


sync_engine = create_engine('sqlite:///database.db')
sync_inspector = inspect(sync_engine)
Session = sessionmaker(bind=sync_engine)


class DBHelper:
    def __init__(self, engine: Engine = sync_engine, inspector: Inspector = sync_inspector):
        self.engine = engine
        self.inspector = inspector

    def drop_tables(self):
        Base.metadata.drop_all(self.engine)

    def create_tables(self):
        self.drop_tables()
        Base.metadata.create_all(self.engine)

    def is_tables(self):
        if self.inspector.get_table_names():
            return True

        return False


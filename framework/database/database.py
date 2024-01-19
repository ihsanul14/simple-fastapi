from decouple import config
from sqlalchemy import create_engine


class Database:
    def postgres(self):
        engine = create_engine(config('PG_URI'))
        return engine

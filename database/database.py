import psycopg2
import psycopg2.extras
from psycopg2.extras import RealDictCursor
from decouple import config


def connect_pg():
    con = psycopg2.connect(host=config("PG_HOST"),
                           database=config("PG_DB"),
                           user=config("PG_USER"),
                           password=config("PG_PASSWORD"),
                           port=int(config("PG_PORT")), cursor_factory=RealDictCursor)
    return con

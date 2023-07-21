import pandas as pd
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def connect_to_database(dbname, user, host, password):
    try:
        con = psycopg2.connect(dbname=dbname, user=user, host=host, password=password, port='5432')
    except psycopg2.OperationalError:
        con = psycopg2.connect(dbname='postgres', user=user, host=host, password=password)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname)))
        con.close()
        con = psycopg2.connect(dbname=dbname, user=user, host=host, password=password)

    return con

def insert_data_to_db(con, df):
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS bundes_bank (
            id SERIAL PRIMARY KEY,
            dataflow VARCHAR(255),
            dim1 VARCHAR(255),
            time_period VARCHAR(255),
            obs_value INT
        )
    ''')

    for index, row in df.iterrows():
        cur.execute('''
            INSERT INTO bundes_bank (dataflow, dim1, time_period, obs_value)
            SELECT %s, %s, %s, %s
            WHERE NOT EXISTS (
                SELECT 1 FROM bundes_bank WHERE dataflow=%s AND dim1=%s AND time_period=%s AND obs_value=%s
            )
        ''', (row['DATAFLOW'], row['DIM1'], row['TIME_PERIOD'], row['OBS_VALUE'], row['DATAFLOW'], row['DIM1'], row['TIME_PERIOD'], row['OBS_VALUE']))

    con.commit()

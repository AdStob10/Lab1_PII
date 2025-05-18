import sqlite3
import pandas as pd

def get_conn():
    yield sqlite3.connect('sales.db')


def get_data():
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM sales')
        data = cur.fetchall()
        return pd.DataFrame(data)
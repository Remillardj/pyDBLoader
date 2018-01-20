import sqlite3

def init_conn(PATH_TO_DB):
    try:
        conn = sqlite3.connect(PATH_TO_DB)
        return True
    except sqlite3.OperationalError as e:
        print(e)

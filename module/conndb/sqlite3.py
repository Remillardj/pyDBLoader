import sqlite3
import sys

sys.path.append("../")
import pyDBLogger

def check_path(PATH_TO_DB):
    if (os.path.exists(PATH_TO_DB) == False):
        logger.debug("")

def init_conn(PATH_TO_DB):
    try:
        conn = sqlite3.connect(PATH_TO_DB)
        return True
    except sqlite3.OperationalError as e:
        print(e)

import time
import sqlite3
import logging

# Program does require sudo priviledges
db_path = "./log/pyDBLogger.db"
log_file_path = "/var/log/pydbloader.log"
log_error_level = "DEBUG"
log_to_db = True

'''
 If the database file does not exist, return True, else return False
'''
def dbExist(dbPath):
    return os.path.isfile(dbPath)

'''
 If the database file does not exist, then create one.
'''
if (dbExist(db_path) == False):
    print ("No SQLite3 logging database! Creating one...")
    log_db = sqlite3.connect(db_path)
    cursor = log_db.cursor()
    cursor.execute('''
                    CREATE TABLE pydblogger(id INTEGER PRIMARY KEY,
                    log_level VARCHAR(50), log_levelname VARCHAR(50),
                    log_message TEXT, created_at VARCHAR(50), created_by VARCHAR(50));
                       ''')

class pyDBLogger(logging.Handler):
    def __init__(self, sqlConn, sqlCursor, dbTblLog):
        logging.Handler.__init__(self)
        self.sqlConn = sqlConn
        self.sqlCursor = sqlCursor
        self.dbTblLog = dbTblLog

    # ToDo: Sanitization of message to prevent SQL injection
    def purell(self, message):
        return str(mesage)

    def vent(self, message):
        tictoc = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))

        message = purell(message)

        sqlInsertQuery = 'INSERT INTO ' + self.db_tbl_log + ' (log_level, ' + \
            'log_levelname, log, created_at, created_by) ' + \
            'VALUES (' + \
            ''   + str(record.levelno) + ', ' + \
            '\'' + str(record.levelname) + '\', ' + \
            '\'' + str(self.log_msg) + '\', ' + \
            '(convert(datetime2(7), \'' + tm + '\')), ' + \
            '\'' + str(record.name) + '\')'

        try:
            self.sqlCursor.execute(sqlInsertQuery)
            self.sqlConn.commit()
        except mysqldb.Error as e:
            print ("Failed to insert into database:", e)

if (log_to_db):
    log_conn = mysqldb.connect(db_server, db_user, db_password, db_dbname)
    log_cursor = log_conn.cursor()
    logdb = pyDBLogger(log_conn, log_cursor, db_tbl_log)

logging.basicConfig(filename=log_file_path)

if (log_to_db):
    logging.getLogger('').addHandler(logdb)
    log = logging.getLogger("pyDBLogger")
    log.setLevel(log_error_level)

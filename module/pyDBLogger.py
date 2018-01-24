import time
import mysqldb
import logging

# Some settings
db_server = "localhost:8080"
db_user = "username"
db_password = "password"
db_dbname = "dbname"
db_tbl_log = "pyDBLogger"

# Program does require sudo priviledges
log_file_path = "/var/log/pydbloader.log"
log_error_level = "DEBUG"
log_to_db = True

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

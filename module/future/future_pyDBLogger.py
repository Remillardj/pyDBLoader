'''
 Placed here for future time to log to an SQLite3 database
'''

# Program does require sudo priviledges
db_path = "logs/pyDBLogger.db"
log_file_path = "/var/log/pydbloader.log"
log_error_level = "DEBUG"
log_to_db = True

# log settings
log("db_path = "+db_path)
log("log_file_path = "+log_file_path)
log("log_error_level = "+log_error_level)
log("log_to_db = "+str(log_to_db))


# If the database file does not exist, return True, else return False
def dbExist(dbPath):
    log("Checking if database exists.", "DEBUG")
    return os.path.isfile(dbPath)

# If the database file does not exist, then create one.
if (dbExist(db_path) == False):
    print ("No SQLite3 logging database! Creating one...")
    log("No SQLite3 logging database! Creating one...")
    try:
        log_db = sqlite3.connect(db_path)
        cursor = log_db.cursor()
        cursor.execute('''
                        CREATE TABLE pydblogger (
                            id integer PRIMARY KEY AUTOINCREMENT,
                            asctime datetime,
                            relative_created varchar,
                            process_id integer,
                            process_name varchar,
                            thread_id integer,
                            path_name varchar,
                            file_name varchar,
                            function_name varchar,
                            level_name varchar,
                            level_no varchar,
                            message text,
                            linenumber integer
                        ''');)

    except sqlite3.OperationalError as e:
        log("Failed to create database! Error: " + e, "ERROR")

log("Logging database exists! Connecting to database...")
try:
    log_db = sqlite3.connect(db_path)
    cursor = log_db.cursor()
except sqlite3.OperationalError as e:
    log("Failed to connect to logging database!"+e, "ERROR")
log("Successfully connected to the logging database!... Starting to log to database.")

# Purpose: To be able to log to a database
# Input:
#    dbCursor -> database cursor
#    tableName -> table name to log too
#    logLevel -> Level of the log severity
#    logMessage ->

class pyDBLogger(cursor):
    def __init__(self, cursor, db_tbl_log, levelno, levelname, log_msg, name):
        self.cursor = cursor
        self.db_tbl_log = db_tbl_log
        self.levelno = levelno
        self.levelname = levelname
        self.log_msg = log_msg
        self.name = name

    # ToDo: Sanitization of message to prevent SQL injection
    def purell(self, message):
        return str(message)

    def vent(self, cursor, message):
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
        except sqlite3.OperationalError as e:
            log("Failed to insert into database:" + e, "ERROR")


'''

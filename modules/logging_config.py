import logging
import os
import sys

log_filename = "./logs/pydbloader-main.log"

# Check if the environment variable is set. If it is, then use it to log to the location.
# If it is not set, then use the default.
try:
    if (os.getenv('log_file_default') != None):
        if (os.environ['log_file_default'] == "./logs/pydbloader-main.log"):
            log_filename = "./logs/pydbloader-main.log"
    else:
        print ("log_file_default environment variable not set, setting to default: " + log_filename)
        os.environ['log_file_default'] = log_filename
except KeyError as e:
    print ("Error: " + e)

'''
 Check if verbosity is set, and if it is, log to file and console
'''
file_handler = logging.FileHandler(filename=log_filename)
try:
    if (os.environ['verbose'] != None):
        stdout_handler = logging.StreamHandler(sys.stdout)
        handlers = [file_handler, stdout_handler]
except KeyError as e:
    print ("verbose environment variable not set, setting to default: False")
    handlers = [file_handler]

logging.basicConfig(
    level=logging.DEBUG,
    format="%(created)f : %(asctime)s : %(relativeCreated)d | %(process)d - %(processName)s - %(thread)d - %(threadName)s | %(pathname)s - %(filename)s - %(funcName)s [%(lineno)d]:[%(levelname)s/%(levelno)s]:%(message)s",
    handlers=handlers,
    )

# For some reason this got deleted? I'm not sure why, but it was originally in pyDBLoader.
# message is a string to place into the log, level is set to debug by default, but can be set to
# other levels
def log(message, level="DEBUG"):
    if (level == "DEBUG"):
        logging.debug(message)
    elif (level == "INFO"):
        logging.info(message)
    elif (level == "WARNING"):
        logging.warning(message)
    elif (level == "CRITICAL"):
        logging.critical(message)
    elif (level == "ERROR"):
        ogging.error(message)
    else:
        logging.error("Log failed to input message")
        print("Log failed to input message")
        return False

log("Logging is set up!")

# Will implement a configuration file later date, just want
# to get this up and running.

'''
config = configparser.ConfigParser()
config.read("../config/logger_config.ini")
logging.config.fileConfig(config)

fileConfig('config/logging_config.ini')
logger = logging.getLogger()
'''

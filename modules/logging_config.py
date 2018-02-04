import logging
import os
import sys

log_filename = "./logs/pydbloader-main.log"
if (os.environ['log_file_default'] == "./logs/pydbloader-main.log"):
    log_filename = "./logs/pydbloader-main.log"
else:
    log_filename = os.environ['log_file_default']

'''
 Check if verbosity is set, and if it is, log to file and console
'''
if (os.environ['verbose'] is not False):
    file_handler = logging.FileHandler(filename=log_filename)
    stdout_handler = logging.StreamHandler(sys.stdout)
    handlers = [file_handler, stdout_handler]
else:
    file_handler = logging.FileHandler(filename=log_filename)
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
        logging_config.logging.debug(message)
    elif (level == "INFO"):
        logging_config.logging.info(message)
    elif (level == "WARNING"):
        logging_config.logging.warning(message)
    elif (level == "CRITICAL"):
        logging_config.logging.critical(message)
    elif (level == "ERROR"):
        logging_config.logging.error(message)
    else:
        logging_config.logging.error("Log failed to input message")
        print("Log failed to input message")
        return False

# Will implement a configuration file later date, just want
# to get this up and running.

'''
config = configparser.ConfigParser()
config.read("../config/logger_config.ini")
logging.config.fileConfig(config)

fileConfig('config/logging_config.ini')
logger = logging.getLogger()
'''

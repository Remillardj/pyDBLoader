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
    format="%(created)f : %(asctime)s : %(relativeCreated)d | %(process)d - %(processName)s - %(thread)d - %(threadName)s | %(pathname)s - %(filename)s - %(funcName)s:[%(levelname)s/%(levelno)s]:%(message)s [%(lineno)d]",
    handlers=handlers,
    )

# Will implement a configuration file later date, just want
# to get this up and running.

'''
config = configparser.ConfigParser()
config.read("../config/logger_config.ini")
logging.config.fileConfig(config)

fileConfig('config/logging_config.ini')
logger = logging.getLogger()
'''

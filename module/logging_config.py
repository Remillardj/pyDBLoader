import logging

logging.basicConfig(
    filename="logs/pydbloader-main.log",
    level=logging.DEBUG,
    format="%(created)f : %(asctime)s : %(relativeCreated)d | %(process)d - %(processName)s - %(thread)d - %(threadName)s | %(pathname)s - %(filename)s - %(funcName)s:[%(levelname)s/%(levelno)s]:%(message)s [%(lineno)d]"
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

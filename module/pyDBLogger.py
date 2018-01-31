#import time
#import sqlite3
import logging
#import os

import logging_config

'''
 Purpose: Function to log quickly instead of repeatively typing out
 logging config python file, followed by objects.

 Input:
    message -> str; the message to go into the logger
    level -> str;
'''
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
        return False;

# File logger successful!
log("Successfully loaded logging_config.py on pyDBLogger!")

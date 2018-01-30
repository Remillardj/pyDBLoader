import logging
from logging.config import fileConfig

fileConfig('../config/logging_config.ini')
logger = logging.getLogger()

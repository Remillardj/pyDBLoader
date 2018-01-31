import sys
import os
import yaml

# custom module
import pyDBLogger as log

# Program starting log entry
log.log("Loading up pyDBLoader...")

class pyDBLoader():
    def __init__(self, dbType, dbPath, dbUsername, dbPassword, config):
        self.dbType = dbType
        self.dbPath = dbPath
        self.dbUsername = dbUsername
        self.dbPassword = dbPassword
        self.config = config

    '''
     A function to verify if specified file is indeed a file
     Returns false is not, returns true if it is
    '''
    def verify_file(self, dbPath):
        log.log("Checking if "+dbPath+" is a file: "+str(os.path.isfile(dbPath)))
        return os.path.isfile(dbPath)

    '''
     Loads configuration file
     Returns with the configuration options if successful,
     returns false if it is not
    '''
    def load_config(self, config):
        log.log("Loading configuration file.")
        if (verify_file(config)):
            try:
                with open(config, 'r') as conf:
                    options = yaml.load(conf)
            except:
                #todo log action
                return False
            return options

    '''
     Will do the bulk of the work in delegating and sorting what database to input,
     and base it off the configuration
    '''
    def main(self, dbType, config):
        log.log("Starting pyDBLoader test load")
        if (verify_file(config)):
            if (load_config(config)):
                options = load_config(config)

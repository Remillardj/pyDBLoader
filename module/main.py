import sys
import os
import yaml

# custom module
import pyDBLogger as log

# Program starting log entry
log.log("Loading up pyDBLoader...")

class pyDBLoader:
    def __init__(self, dbType, dbPath, config, dbUsername=None, dbPassword=None):
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
        if (self.verify_file(config)):
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
    def main(self):
        log.log("Starting pyDBLoader test load")
        if (self.verify_file(self.config)):
            log.log("Verified configuration file: "+str(self.config))
            if (self.load_config(self.config)):
                options = self.load_config(self.config)
                log.log("Loaded configurations!: "+str(options))
                print (options)
            else:
                log.log("Could not load configuration files. Using defaults.")
        else:
            log.log("Could not verify configuration file. Using defaults.")

py = pyDBLoader("sqlite3", "test/sqlite3_test.db", "config/logger_config.ini")
py.main()

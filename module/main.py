import sys
import os
import yaml

# custom module
import pyDBLogger as log

# Program starting log entry
log.log("Loading up pyDBLoader...")

class pyDBLoader:
    def __init__(self, dbType, dbPath=None, config=None, dbUsername=None, dbPassword=None, dbPort=None):
        self.dbType = dbType
        self.dbPath = dbPath
        self.dbUsername = dbUsername
        self.dbPassword = dbPassword
        self.config = config

    def get_dbType(self):
        log.log("Getter dbType called!")
        return self.dbType

    def get_dbPath(self):
        log.log("Getter dbPath called!")
        return self.dbPath

    def get_dbUsername(self):
        log.log("Getter dbUsername called!")
        return self.dbUsername

    def get_config(self):
        log.log("Getter config called!")
        return self.config

    '''
     A function to verify if specified file is indeed a file
     Returns false is not, returns true if it is
    '''
    def verify_file(self, dbPath):
        log.log("Checking if ''"+dbPath+"'' is a file: "+str(os.path.isfile(dbPath)))
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
                    return options
            except:
                #todo log action
                return False
        log.log("Something went wrong! Could not open configuration file!")

    '''
     Will do the bulk of the work in delegating and sorting what database to input,
     and base it off the configuration
    '''
    def main(self):
        log.log("Starting pyDBLoader test load")

        log.log("Loading up the configuration file!")
        if (self.verify_file(self.config)):
            log.log("Verified configuration file: "+str(self.config))
            if (self.load_config(self.config)):
                options = self.load_config(self.config)
                print(options)
                log.log("Loaded configurations!: "+str(options))
                print (options)
            else:
                log.log("Could not load configuration files. Using defaults.")
        else:
            log.log("Could not verify configuration file. Using defaults.")

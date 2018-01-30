import sys
import loader.loader
import os
import yaml

from module import pyDBLogger as pdb


class pydbloader():
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
        #todo log action
        return os.path.isfile(dbPath)

    '''
     Loads configuration file
     Returns with the configuration options if successful,
     returns false if it is not
    '''
    def load_config(self, config):
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
    def main(self):
        pass

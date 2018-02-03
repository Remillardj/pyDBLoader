import argparse
import sys
import module.logging_config as log
import os

# Set up default variables
version = "pyDBLoader 0.0.2 [AlphaDev]"
config_file_default = './config/logger_config.yml'
log_file_default = "./logs/pydbloader-main.log"

# Set environment variables
os.environ['config_file_default'] = config_file_default
os.environ['log_file_default'] = log_file_default

def file_exists(file):
    log.log("Checking if file exists: " + file + "... " + os.path.exists(file))
    return os.path.exists(file)

def banner():
    print ("---------------------------------")
    print ("|    Welcome to pyDBLoader!     |")
    print ("---------------------------------")
    print ("\n")
    print ("#################################")
    print ("##   Help Menu for pyDBLoader  ##")
    print ("#################################")

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(prog='pyDBLoader', add_help=True, allow_abbrev=False, description='pyDBLoader Help Menu')
    parser.add_argument('--version', action='version', version=version)

    parser.add_argument('--banner', help='Display the programs banner')

    # If the user wants to a config file they can
    parser.add_argument('-c', '--config', default=config_file_default, required=False,
                        help='Load configuration file to load user-specified databases, with information needed for connection.')

    parser.add_argument('-l', '--log', default=log_file_default,
                        help='Log the program to a file. Default is located in ./logs/pydbloader-main.log')
    # ToDo
    #parser.add_argument('--logdb', default=False, help='Log to an SQLite3 database')
    #parser.add_argument('-v', '--verbose', help='Allow for more verbose actions', default=False)

    parser.add_argument('--dbtype', default='sqlite3', choices=['sqlite3', 'postgresql', 'mysql'])

    # add database implementation
    parser.add_argument('--sqlite3', help='Insert your database file into an SQLite3 database')
    parser.add_argument('-f', '--filepath', help='The location of your database file')
    args = parser.parse_args()

    # Process argparse for banner
    if (args.banner):
        banner()

    # Process configuration file argument
    if (args.config != config_file_default):
        if (file_exists(args.config) == False):
            log.log("Setting environment variable 'config_file_default' => " + args.config)
            os.environ['config_file_default'] = args.config
        else:
            print("Specified log file exists! Using default: " + config_file_default)
            log.log("Specified log file exists! Using default: " + config_file_default)


    # Process log file path argument
    if (args.log != log_file_default):
        if (file_exists(args.log) == False)
            log.log("Setting environment variable 'log_file_default' => " + args.log)
            os.environ['log_file_default'] = args.log
        else:
            print("Specified log file exists! Using default: " + log_file_default)
            log.log("Specified log file exists! Using default: " + log_file_default)

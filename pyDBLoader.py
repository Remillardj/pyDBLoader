#! /usr/bin/env python3

import argparse
import sys
import os

# Ugh I don't want to do this but I got no choice for debugging
sys.path.append("/Users/remillardj/Tech/Repo/pyDBLoader/modules/")
print(sys.path)

import loader

# Set up default variables
version = "pyDBLoader 0.0.2 [AlphaDev]"
config_file_default = "./config/logger_config.yml"
log_file_default = "./logs/pydbloader-main.log"

# Set environment variables
os.environ['config_file_default'] = config_file_default
os.environ['verbose'] = "False"
os.environ['db_type'] = "None"
os.environ['file_path'] = "None"
os.environ['port'] = "None"
os.environ['username'] = "None"
os.environ['password'] = "None"

# Log to file as default
os.environ['log_file_default'] = log_file_default
import logging_config as log

sys.exit()

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

parser = argparse.ArgumentParser(prog='pyDBLoader', add_help=True, description='pyDBLoader Help Menu')
parser.add_argument('--version', action='version', version=version)

# If the user wants to a config file they can
parser.add_argument('-c', '--config', type=str, default=config_file_default, required=False,
                    help='Load configuration file to load user-specified databases, with information needed for connection.')

parser.add_argument('-l', '--log', type=str, default=log_file_default,
                    help='Log the program to a file. Default is located in ./logs/pydbloader-main.log')
# ToDo
#parser.add_argument('--logdb', default=False, help='Log to an SQLite3 database')
parser.add_argument('-v', '--verbose', help='Allow for more verbose actions', default=False)

parser.add_argument('--dbtype', choices=['sqlite3', 'postgresql', 'mysql'])

# add database implementation
parser.add_argument('--sqlite3', help='Insert your database file into an SQLite3 database', default=False)
parser.add_argument('-f', '--filepath', help='The location of your database file', type=str)
parser.add_argument('-p', '--port', help="Port for the database if necessary", type=int)

parser.add_argument('-u', '--username', help="Username for the database", type=str)
parser.add_argument('--password', help="Password for the database", type=str)
args = parser.parse_args()

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
    if (file_exists(args.log) == False):
        log.log("Setting environment variable 'log_file_default' => " + args.log)
        os.environ['log_file_default'] = args.log
    else:
        print("Specified log file exists! Using default: " + log_file_default)
        log.log("Specified log file exists! Using default: " + log_file_default)

if (args.verbose is not False):
    os.environ['verbose'] = args.verbose

# Process db type argument, convert to string as it picks from a list
os.environ['db_type'] = str(args.dbtype)

# Process filepath argument, if is set, then set environment variable
if (args.filepath):
    os.environ['file_path'] = args.filepath

# Process port argument
if (args.port):
    os.environ['port'] = args.port

# Process username argument
if (args.username):
    os.environ['username'] = args.username

# Process password argument
if (args.password):
    os.environ['password'] = args.password

if (__name__ == "__main__"):
    import loader
    pydb.pyDBLoader("sqlite3", "test/sqlite3_test.db", "./config/logger_config.yml")
    pydb.loader()

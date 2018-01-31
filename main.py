import argparse
import module.logging_config as log

def banner():
    print ("---------------------------------")
    print ("|    Welcome to pyDBLoader!     |")
    print ("---------------------------------")
    print ("\n")
    print ("#################################")
    print ("##   Help Menu for pyDBLoader  ##")
    print ("#################################")

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(description='pyDBLoader Help Menu')
    parser.add_argument('-c', '--config', default='./config/logger_config.yml',
                        help='Load configuration file to load user-specified databases, with information needed for connection.')
    parser.add_argument('-l', '--log', default='./logs/pydbloader-main.log',
                        help='[DEPRECATED: Log the program. Default is located in ./logs/pydbloader-main.log')
    parser.add_argument('-v', '--verbose', help='[DEPRECATED] Allow for more verbose actions', default=False)
    args = parser.parse_args()

    '''
	parser = argparse.ArgumentParser(description='pyDBLoader help menu')
	parser.add_argument('--sqlite3', help='Insert your database into an SQLite3 database')
    parser.add_argument('--filepath', help='The location of your database')
	args = parser.parse_args()
    '''

# Call banner
banner()

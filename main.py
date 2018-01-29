import argparse
from modules import *

def banner():
    print ("#################################")
    print ("##     Help Menu for pyDBLoader     ##")
    print ("#################################")

if (__name__ == "__main__"):
	parser = argparse.ArgumentParser(description='pyDBLoader help menu')
	parser.add_argument('--sqlite3', help='Insert your database into an SQLite3 database')
    parser.add_argument('--mysql', help='Insert your database into an MySQL database')
    parser.add_argument('--filepath', help='The location of your database')
	args = parser.parse_args()

banner()

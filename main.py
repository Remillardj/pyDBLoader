import argparse
from modules import *

def banner():
    print ("---------------------------------")
    print ("|    Welcome to pyDBLoader!     |")
    print ("---------------------------------")
    print ("\n")
    print ("#################################")
    print ("##   Help Menu for pyDBLoader  ##")
    print ("#################################")

if (__name__ == "__main__"):
	parser = argparse.ArgumentParser(description='pyDBLoader help menu')
	parser.add_argument('--sqlite3', help='Insert your database into an SQLite3 database')
    parser.add_argument('--filepath', help='The location of your database')
	args = parser.parse_args()

banner()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name = 'pydbloader',
      version = '0.0.2',
      description = 'A python database loader for various relational databases',
      url = 'https://github.com/Remillardj/pyDBLoader',
      author = 'Jaryd Remillard',
      license = 'Apache',
      install_requires = [ requirements ],
)

import os
NAME_DB = 'botshop.sqlite'

VERSION = '1.0'

AUTHOR = 'mvandron'


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB = "shopdb"
DATABASE = os.path.join('sqlite:///'+BASE_DIR,DB,NAME_DB)
print(DATABASE)

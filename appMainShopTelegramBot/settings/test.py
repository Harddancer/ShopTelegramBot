import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join('sqlite:///'+BASE_DIR, "shopdb","shop.sql")
print(DATABASE)

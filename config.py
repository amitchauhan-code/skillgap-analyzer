import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'super-secret-key')
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Chauhan@123'
    MYSQL_DB = 'skillgap'
    MYSQL_CURSORCLASS = 'DictCursor'

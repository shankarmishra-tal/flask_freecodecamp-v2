import os
from dotenv import load_dotenv
# SECRET_KEY=environ.get('SECRET_KEY)
# API_KEY=environ.get('API_KEY')
# MYSQL_USER=environ.get('MYSQL_USER')

load_dotenv()

class Config:
    MYSQL_USERNAME=os.getenv('MYSQL_USERNAME')
    MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD')
    MYSQL_HOST=os.getenv('MYSQL_HOST')
    MYSQL_DB_NAME=os.getenv('MYSQL_DB_NAME')

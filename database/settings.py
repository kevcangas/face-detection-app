#This file contains the information required to connect to the database

#Pydantic
from pydantic import BaseSettings


#Peewee
import peewee


class Settings(BaseSettings):

    db_name: str = 'qr-project'
    db_user: str = 'root'
    db_pass: str = ''
    db_host: str = '127.0.0.1'
    db_port: int = 3306


settings = Settings()

DB_NAME = settings.db_name
DB_USER = settings.db_user
DB_PASS = settings.db_pass
DB_HOST = settings.db_host
DB_PORT = settings.db_port


#If the database used in you rproject is different to MySQL you can change the 
#next line according to your database (see peewee documentation)
db = peewee.MySQLDatabase(DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

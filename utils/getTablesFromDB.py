#Python
import subprocess


#Own libraries
from core.settings import Settings


def run():
    settings = Settings()

    DB_NAME = settings.db_name
    DB_USER = settings.db_user
    DB_PASS = settings.db_pass
    DB_HOST = settings.db_host
    DB_PORT = settings.db_port

    COMMAND = "py -m pwiz -e mysql -u" + str(DB_USER) + " " + str(DB_NAME) + "> utils/mymodels.txt"

    subprocess.run(COMMAND, shell=True)


#This script create a text file that contents all the tables read from the database
if __name__ == '__main__':
    run()
import datetime
from time import sleep

birthday = datetime.datetime(1997,11,15,00,00,00)

while(True):
    print datetime.datetime.today()-birthday
    sleep(5)


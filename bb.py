import datetime
from time import sleep

birthday = datetime.datetime(1997,11,15,00,00,00)
print datetime.timedelta(birthday-datetime.date.today())

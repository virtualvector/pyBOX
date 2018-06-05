from time import sleep,localtime,strftime

print strftime("%a %b %d %m %y",localtime())

from datetime import datetime,date
print date.today().strftime("%a %b")



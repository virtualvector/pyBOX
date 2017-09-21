#!/usr/bin/python           # This is client.py file
from crc import *

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))

while True:
    
    data_word = random_data_word_generator(100)
    divisor = '1'+random_data_word_generator(15)
    data_list = list(data_word)
    divisor_list  = list(divisor)

    code_word = crc_generator(divisor_list,data_list)


    a= "".join(data_word)
    b= "".join(code_word)
    c= "".join(divisor)
    
    print "--"*40
    print "dataword ",a
    print "codeword ",b
    print "generator ",c

    print "--"*40
    #checked_rem="".join(crc_checker(code_word,divisor_list))
    #d= "remainder obtainded at receiver site "+checked_rem[-15:]
       
    time.sleep(5) 
    s.send("^".join((a,b,c)))
s.close         

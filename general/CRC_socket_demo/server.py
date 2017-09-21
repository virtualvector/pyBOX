import socket               # Import socket module

def crc_checker(code_word,divisor_list):
	temp_data_list=[i for i in code_word]
	for i in range(len(temp_data_list)-len(divisor_list)+1):
                if(temp_data_list[i]=='1'):
                        for j in range(len(divisor_list)):
                                if(divisor_list[j]==temp_data_list[i]):
                                        temp_data_list[i]='0'
                                        i+=1
                                else :
                                        temp_data_list[i]='1'
                                        i+=1

                else:
                        temp_data_list[i]='0'
	return temp_data_list

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5) 

c, addr = s.accept()                 # Now wait for client connection.
while True:
    
       # Establish connection with client.
   data=c.recv(1024)
   if data=='comms shutdown':
        print "close"
        c.close()
        raise SystemExit
   else:
        dataword,codeword,generator= [i for i in data.split('^')]
        print "--"*40
        print "codeword  ",codeword
        print "generator ",generator
        
        checked_rem="".join(crc_checker(list(codeword),list(generator)))
        print "remainder obtainded  ",checked_rem[-15:] 

        print "--"*40




























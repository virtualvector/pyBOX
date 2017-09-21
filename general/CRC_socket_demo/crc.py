import random
import time
def crc_generator(divisor_list,data_list):

	temp_data_list =[i for i in data_list]
	temp_data_list+='0'*(len(divisor_list)-1)

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

	
	return data_list+temp_data_list[-15:]
	

def random_data_word_generator(n):
	string =""
	for i in range(0,n):
		string+=str(random.randint(0,1))


	return string


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

if __name__=='__main__':

	for i in range(100):
		data_word = random_data_word_generator(100)
		divisor = '1'+random_data_word_generator(15)
		data_list = list(data_word)
		divisor_list  = list(divisor)



		code_word = crc_generator(divisor_list,data_list)


		print "dataword : ","".join(data_word)
		print "codeword : ","".join(code_word)
		print "generator : ","".join(divisor)
	
		
		checked_rem="".join(crc_checker(code_word,divisor_list))
		print "remainder obtainded at receiver site ",checked_rem[-15:]
	
		time.sleep(5)








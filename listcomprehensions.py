numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]


#print all positive numbers in numbers
print [i for i in numbers if(i>0) ]

#above challenge using filter 
print list(filter(lambda x: x>0,numbers))




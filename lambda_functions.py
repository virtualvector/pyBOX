#defining a lambda function
func=lambda x : x**2

#lambda functions using filter

new_list=list(filter(lambda x: x%3==0 ,[1,2,3,4,5]))
print new_list


#map function using lambda function
new_list = list(map(lambda x:pow(x,3),[1,2,3,4,5]))
print new_list


#print the powers of 3 using lambda func
print list(map(lambda x:pow(x,3),[i for i in range(10)]))

#print all the  numbers divisible by 3
print list(filter(lambda x:x%3==0,[ i for i in range(60)]))

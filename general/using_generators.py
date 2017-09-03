
# coding: utf-8

# In[1]:

#Generator demo


# In[6]:

def fiboGenerator():
    a=0
    b=1
    while True:
        yield a
        a,b=b,a+b


# In[7]:

fiboGen=fiboGenerator()


# In[8]:

for i in range(20):
    print fiboGen.next()


# In[15]:

def primeGenerator():
    for i in range(2,100000):
        if(checkPrime(i)):
            yield i


# In[24]:

def checkPrime(i):
    for j in range(2,(i)):
        if i%j == 0 :
            return False
    return True
        


# In[25]:

primeGen=primeGenerator()
for i in range(200):
    print primeGen.next()


# In[ ]:




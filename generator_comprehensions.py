gene = (i for i in range(0,1000000))
print gene.next()

try:
    while(True):
        print gene.next()
except StopIteration as e:
    pass



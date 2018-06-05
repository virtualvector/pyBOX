ll = [1,2,3,4,5,6,6,6]

#lambda demo
ll.sort(lambda x,y :-1 if x>y else 1)
print ll

#map
ll=map(lambda x: x**2,ll)
print ll

#filter
ll=filter(lambda x: False if x<10 else True,ll)
print ll

#reduce
ll = reduce(lambda x,y: x+y,ll)
print ll


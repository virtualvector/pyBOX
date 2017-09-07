def comparator(a,b):
    if(len(a)==len(b)):
        if(a<b):return -1
        else: return 1

    return len(a)-len(b)



ll=['a','aaa','b','bbb','d','cc']
print sorted(ll,cmp=comparator)

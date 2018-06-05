from collections import defaultdict


def main():
    #list demo
    ll = list()
    #append
    ll.append(2)

    #extend
    ll2 = [1,2,3,4,5]
    ll.extend(ll2)

    #print
    print ll

    #pop
    print ll.pop(0)
    
    #count
    print ll.count(2)

    #insert
    ll.insert(0,222)
    print ll

    """
    dict practice
    
    """
    dict1 = {3:"bye", 4:"cya"}
    dict1[2]="hello"
    print dict1[2]

    for key,value in dict1.items():
        print key,value

    print dict1.keys()
    print dict1.values()
    print dict1.items()

    "defualt dict"

    dict2 = defaultdict(int)

    for i in range(0,100):
        dict2[i]+=1

    print dict2
    
    print help('collections')
    


if __name__=="__main__":
    main()

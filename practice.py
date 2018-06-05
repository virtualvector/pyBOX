from collections import defaultdict

def func(a,b):
    return 1 if a>b else -1


def main():
    
    s= "hello"
    ll = [5,4,3,2,1]
    ll.sort(func)
    print ll



if __name__=="__main__":
    main()

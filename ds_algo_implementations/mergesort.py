"""
MergeSort implementation in python 

Author : Rohith Raj R
Date   : 23/06/2017

"""

from random import randint


def merge(a,l,m,r):
    n1 = m-l+1
    n2 = r-m

    L=list()
    R=list()

    for i in range(n1):
        L.append(a[l+i])

    for j in range(n2):
        R.append(a[m+1+j])

    i=0
    j=0
    k=l

    while(i<n1 and j<n2):
        if(L[i]<=R[j]):
            a[k]=L[i]
            k+=1
            i+=1
        else:
            a[k]=R[j]
            k+=1
            j+=1


    while(i<n1):
        a[k]=L[i]
        k+=1
        i+=1

    while(j<n2):
        a[k]=R[j]
        k+=1
        j+=1
    return a



def mergesort(a,l,r):
    if(l<r):
        mid = (l+r)/2;
        mergesort(a,l,mid)
        mergesort(a,mid+1,r)
        merge(a,l,mid,r)
        return a




def main():
   
    a = list()
    for i in range(100):
        a.append(randint(0,100))
    a=mergesort(a,0,len(a)-1)
    print a



if __name__=='__main__':
    main()

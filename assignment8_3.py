'''
Design python application which creates two threads as evenlist and oddlist. Both the
threads accept list of integers as parameter. Evenlist thread add all even elements
from input list and display the addition. Oddlist thread add all odd elements from input
list and display the adition.'''
from threading import *
def even(list1):
    sum=0
    l=len(list1)
    for i in range(0,l):
        if((list1[i]%2)==0):
            sum+=list1[i]
    print("even no addition=",sum)
def odd(list1):
    sum=0
    l=len(list1)
    for i in range(0,l):
        if((list1[i]%2)!=0):
            sum+=list1[i]
    print("Odd no addition=",sum)
    
def main():
    list1=list()
    no=int(input("enter the how no entered="))
    for i in range(0,no):
        n=int(input("enter the n="))
        list1.append(n)
    
    print(list1)
    t1=Thread(target=even , args=(list1,))
    t2=Thread(target=odd , args=(list1,))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
if (__name__)=="__main__":
    main()
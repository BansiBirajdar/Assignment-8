'''1.Design python application which creates two thread named as even and odd. Even
thread will display first 10 even numbers and odd thread will display first 10 odd
numbers.'''
from threading import *
class CheckNo(Exception):
    def __init__(self,value):
        self.value=value
def Even(no):
    j=2
    while(j<=no):
        if((j%2)==0):
            print("Even no:",j)
        j=j+1;

def Odd(no):
    i=2
    while(i<=no):
        if((i%2)!=0):
            print("Odd no:",i)
        i+=1;
        
def main():
    
    try:
        no=int(input("enter the no="));
        if(no<=0):
            raise(CheckNo("Enter a positive no"))
        else:
            t1=Thread(target=Even,args=(no,))
            t2=Thread(target=Odd,args=(no,))
            t1.start()
            t2.start()
    except CheckNo as error:
        print("error occured::",error)

if (__name__)=="__main__":
    main()
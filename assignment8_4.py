'''Design python application which creates three threads as small, capital, digits. All the
threads accepts string as parameter. Small thread display number of small characters,
capital thread display number of capital characters and digits thread display number of
digits. Display id and name of each thread.'''
from threading import *
import os
def small(str):
    
    print('process id of fun:', os.getppid())
    for i in str:
        if(i.islower()):
            print("samll fun id=",get_ident(), i)
        
def capital(str):
    print('process id of fun:', os.getppid())
    for i in str:
        if(i.isupper()):
            print("captial fun id=",get_ident(), i)

def digits(str):
    print('process id of fun:', os.getppid())
    for i in str:
        if(i.isdigit()):
            print("digit fun id=",get_ident(), i)
            
def main():
    print('parent process of fun:', os.getppid())
    print('process id of fun:', os.getpid())
    str=input("enter the string")
    
    t1 = Thread(target=small, args=(str,))
    t2 = Thread(target=capital, args=(str,))
    t3 = Thread(target=digits, args=(str,))
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()

if (__name__)=="__main__":
    main()
print('parent process of fun:', os.getppid())
print('process id of fun:', os.getpid())

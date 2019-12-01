'''Design python application which contains two threads named as thread1 and thread2.
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
screen. After execution of thread1 gets completed then schedule thread2.'''
from threading import *
def counter(fun,lock,no):
    fun(lock,no)

def Dis1(lock,no):
    lock.acquire()
    for i in range(1,no+1):
        print("no:",i)
    lock.release()

def Dis2(lock,no):
    
    lock.acquire()
    print("display in reverse order=")
    while (no>=1):
        print("no:",no)
        no-=1
    lock.release()
        
def main():
    no=int(input("Enter the no="))
    print("Display the no ")
    
    lock=Lock()
    
    thread1 = Thread(target=counter, args=(Dis1,lock,no,))
    thread2 = Thread(target=counter, args=(Dis2,lock,no,))
    
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

if (__name__)=="__main__":
    main()
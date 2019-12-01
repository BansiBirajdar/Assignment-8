'''Design python application which creates two threads as evenfactor and oddfactor.
Both the thread accept one parameter as integer. Evenfactor thread will display
addition of even factors of given number and oddfactor will display addition of odd
factors of given number. After execution of both the thread gets completed main
thread should display message as “exit from main”.'''
from threading import *
class CheckNo(Exception):
    def __init__(self,value):
        self.value=value
        
def Evenf(no):
    j=2
    sum=0
    while(j<=no):
        if((j%2)==0 and (no%j==0)):
            print("evenf fun id=",get_ident(), j)
            sum+=j
        j=j+1;
    print("evenfactor addition is=",sum)
def Oddf(no):
    i=2
    sum=0
    while(i<=no):
        if((i%2)!=0 and (no%i)==0):
            print("oddf fun id=",get_ident(), i)
            sum+=i
        i+=1
    print("oddfactor addition is=",sum)
def main():
    try:
        no=int(input("enter the no="));
        if(no<=0):
            raise(CheckNo("Enter a positive no"))
        else:
            t1=Thread(target=Evenf,args=(no,))
            t2=Thread(target=Oddf,args=(no,))
            
            t1.start()
            t2.start()
            
            t1.join()
            t2.join()
            
    except CheckNo as error:
        print("error occured::",error)
    print("exit from main")
if (__name__)=="__main__":
    main()
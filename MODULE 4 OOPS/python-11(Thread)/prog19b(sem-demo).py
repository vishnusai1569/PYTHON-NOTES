#  Find  outputs (Home  work)
from threading import *
import time
def   f1():  #   It  can  be  executed  by  3  threads
        sem . acquire()
        name = current_thread() . name
        print(name , 'is   under   execution')
        time . sleep(1)
        print(name , 'finished  execution')
        sem . release()
sem = Semaphore(3)  # It  can  be  locked  3  times
t1 = Thread(target = f1 , name = 'One')  #  Creates  9  threads
t2 = Thread(target = f1 , name = 'Two')
t3 = Thread(target = f1 , name = 'Three')
t4 = Thread(target = f1 , name = 'Four')
t5 = Thread(target = f1 , name = 'Five')
t6 = Thread(target = f1 , name = 'Six')
t7 = Thread(target = f1 , name = 'Seven')
t8 = Thread(target = f1 , name = 'Eight')
t9 = Thread(target = f1 , name = 'Nine')
t1 . start()  #  t1  executes   f1()
t2 . start()  #  t2  executes   f1()
t3 . start()  #  t3  executes   f1()
t4 . start()  #  t4  executes   f1()
t5 . start()  #  t5  executes   f1()
t6 . start()  #  t6  executes   f1()
t7 . start()  #  t7  executes   f1()
t8 . start()  #  t8  executes   f1()
t9 . start()   #  t9  executes   f1()



'''
One is   under   execution
Two is   under   execution
Three is   under   execution
Two finished  execution
One finished  execution
Three finished  execution
Five is   under   execution
Six is   under   execution
Four is   under   execution
Four finished  execution
Six finished  execution
Five finished  execution
Eight is   under   execution
Nine is   under   execution
Seven is   under   execution
Seven finished  execution
Nine finished  execution
Eight finished  execution
'''
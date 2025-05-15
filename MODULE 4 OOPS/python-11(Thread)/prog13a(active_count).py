# Find  outputs  (Home  work)
from  threading  import  *
import  time
def   display():  #  Executed  by  t1 , t2  and  t3  concurrently
        name = current_thread() . name
        print(name , ' is  started')
        time . sleep(3)
        print(name , ' is  ended')
print(active_count())  #  1
t1 = Thread(target = display , name = 'Child Thread 1')  #   Creates  3  new  threads
t2 = Thread(target = display , name = 'Child Thread 2')
t3 = Thread(target = display , name = 'Child Thread 3')
print(active_count())#   1  :   Only  main  thread  as  t1 , t2   and  t3  are  not  started
t1 . start() #   t1  executes   display()  function
t2 . start()  #   t2  executes   display()  function
t3 . start()  #   t3  executes   display()  function
print(active_count())  #   4 :  main() , t1  , t2  and  t3
t1 . join()   # main  thread  waits  for  expiry  of   t1  , t2 and  t3   threads
t2 . join()
t3 . join()
print(active_count())  # 1 :  Only  main  thread  as  t1 , t2   and  t3  are  dead

'''
1
1
Child Thread 1 is  started
Child Thread 2 is  started
Child Thread 3 is  started
4
Child Thread 1 is  ended
Child Thread 2 is  ended
Child Thread 3 is  ended
1



1) What  is  the  order  in  which  threads  resume  after  3  sec ?  --->
																			No  idea  becoz  TS  can  pick  any  thread  after  3 sec

2) Can  outputs  be  predicted  after  3  sec  sleep  time ?  --->  No
'''
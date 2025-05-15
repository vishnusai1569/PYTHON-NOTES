#  Find  outputs
from  threading  import *
import  time
def    fact(n):
	sem . acquire()
	if   n  >  0:
		x = n * fact(n - 1)
	else:
		x = 1
	sem . release()
	return   x
#end of the function
def    disp(n):
	print(n , ' != ' , fact(n))
sem = Semaphore(8)   #  It  can  be locked  8  times
t1 = Thread(target = disp , args = (4,)) #  Creates  2  new  threads
t2 = Thread(target = disp , args = (7,))
t1 . start() #   t1  executes  disp(4)
t2 . start()  #   t2  executes  disp(7)

'''
4  !=  24
7  !=  5040



1) sem = Semaphore(8)
    Can  t1  determine  4! ?  --->  Yes  becoz  4!  requires  5  locks  on  sem  object  and   5 <= 8  is  True
    Can  t2  determine  7! ?  ---> Yes  becoz  7!  requires  8  locks  on  sem  object  and  8 <= 8  is  True

2) sem = Semaphore(7)
    Can  t1  determine  4! ?  ---> Yes  becoz  4!  requires  5  locks  on  sem  object  and   5 <= 7  is  True
    Can  t2  determine  7! ?  ---> No  becoz  7!  requires  8  locks  on  sem  object  and  8 <= 7  is  False.
										         Hence  t2  waits  forever  after  locking  sem  object  for  7  times

3) sem = Semaphore(4)
    Can  t1  determine  4! ?  --->  No  becoz  4!  requires  5  locks  on  sem  object  and  5 <= 4  is  False.
												  Hence  t1  waits  forever  after  locking  sem  object  for  4  times
    Can  t2  determine  7! ?  --->  No  becoz  t2  never  get  a  chance  as  sem  object  is  already
												  locked  for 4  times  by  t1

4) sem = Semaphore()
    Can  t1  determine  4! ?  --->  No  becoz  4!  requires  5  locks  on  sem  object  and  5 <= 1  is  False.
												  Hence  t1  waits  after  locking  sem  object  once
    Can  t2  determine  7! ?  --->  No  becoz  t2  never  get  a  chance  as  sem  object  is  already  locked  once  by  t1
'''
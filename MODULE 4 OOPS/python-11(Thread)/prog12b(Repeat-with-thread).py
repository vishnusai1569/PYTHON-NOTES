'''
Repeat  prog12a(double-square)  such  that  t1  should  execute  double()  function  and
t2  should  execute  square()  function
'''
from threading import *
import time
def double():
	for  i  in  range(1 , 7):
		print('Double : ' , 2 * i)
		time . sleep(1)
def square():
	for  i  in  range(1 , 7):
		print('Square : ' , i * i)
		time . sleep(1)
t1 = Thread(target = double)   #  Creates 2  new  threads
t2 = Thread(target = square)
start = time . time()  # Current  time  before  execution  of  t1  and  t2
t1 . start()  #  t1  executes  double()  function
t2 . start()  #  t2  executes  square()  function
t1 . join()  #  main  thread  waits  for  expiry  of  t1  and  t2
t2 . join()
end = time . time()  # Current  time  after  execution  of  t1  and  t2
print('Execution time of 2  threads : ' , end - start)  #  6.some thing


'''
1) How  many  threads  are  in  the  program ? --->  3  i.e.  main  thread ,  t1  and  t2

2) What  is  main  thread  doing ?  --->  Creates  2  threads , starts  both  of  them,
							  							      waits  for  their  expiry  and  prints  execution  time

3) What  does  thread  t1  do ?  --->  Executes  double()  function

4) What  does  thread  t2  do ?  ---> Executes  square()  function

5) What  is  the  execution  time ?  --->  6.something

6) How  are  t1  and  t2  executed ?  --->  concurrently

7) What  is  the  advantage  of  multi-threading ? --->  Fast  in  execution  due  to  concurrent  execution  of  threads
'''
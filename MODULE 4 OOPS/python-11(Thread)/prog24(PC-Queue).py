'''
Producer  Consumer  problem  with  Queue  class  (Home  work)

Assume  that  random  numbers  are  58 , 75 , 29 , 64 , 13 , ....

1) What  does  thread  'p'  do  ?  --->   Inserts  a  value  into  object  'q'  if  object  'q'  is   empty

2) What  does  thread  'p'  do  if  object  'q'  is  not  empty ?  --->  Thread  'p'  sleeps

3) What  does  thread  'c'  do ? --->  Removes  value  from  object  'q'   if  'q'  is  not  empty

4) What  does  thread  'c'  do  if  object  'q'  is  empty ?  ---> Waits
'''
from  threading  import  *
from  random  import  *
from  queue  import  Queue
import  time
def   f1():  #  Executed  by  thread  'p'
	s = current_thread() . name  #  Name  of  thread  'p'  i.e.  'Producer'
	while  True:  # Infinite
		if  q . empty():  #  Insert  an  element  into  object  'q'  only  when  it  is  empty
			x = randint(1 , 100)  #  Random  number  between  1  and   100
			q . put(x)  #  Thread  'p' inserts   'x'  into  object  'q'
			print(s , 'inserts ' , x)
		time . sleep(1)  #  Thread  'p'  sleeps  for  1  sec
def   f2():   #  Executed  by  thread  'c'
	s = current_thread() . name  #  Name  of  thread  'c'  i.e.  'Consumer'
	while  True:   # Infinite
		x = q . get() #   Thread  'c'  removes  first  element   from  obejct  'q'  and  waits  when  object  'q'  is  empty
		print(s , 'removes  ' , x)
q = Queue()   #  Creates  an   object
p = Thread(target = f1 , name = 'Producer')    # Creates 2  neww  threads
c = Thread(target = f2 , name = 'Consumer')
c . start()  # Thread 'c'  executes  function  f2()
p . start()   # Thread 'p'  executes  function  f1()
print('Press  ctrl + break  or  Fn + b  to  stop')
# How  to  resolve  deadlock ?
from  threading  import  *
import  time
def  f1():  # Executed  by  thread  t1
	l1 . acquire()  # t1  locks  object  l1
	time . sleep(1)  #  t1  sleeps  for  1  sec
	l2 . acquire()   # t1  locks  object  l2
	print('1st  thread  is  under  execution')
	l2 . release()   # t1  unlocks  object  l2
	l1 . release()  # t1  unlocks  object  l1
	print('End  of  the  1st  thread')
def  f2():  # Executed  by  thread  t2
	l1 . acquire()  # t2  locks  object  l1
	time . sleep(1)   #  t2  sleeps  for  1  sec
	l2 . acquire()  # t2  locks  object  l2
	print('2nd   thread  is  under  execution')
	l2 . release()  # t2  unlocks  object  l2
	l1 . release()  # t2  unlocks  object  l1
	print('End  of  the  2nd   thread')
l1 = Lock()  #  Creates  2  Lock  objects
l2 = Lock()
t1 = Thread(target = f1)  # Creates  2  new  threads
t2 = Thread(target = f2)
t1 . start()  #  t1  executes  function  f1()
t2 . start()   #  t2  executes  function  f2()
t1 . join()  #  main   thread  waits  for  expiry  of   t1  and  t2
t2 . join()
print('End  of  main  thread')  #  Executed  after  t1  and  t2  are dead


'''
1) How  to  avoid  deadlock  ?  --->  With  ordering  of  locks

2) What  is  ordering  of  locks ?  ---> Every  thread  should  lock  l1  first  and  then  l2
'''
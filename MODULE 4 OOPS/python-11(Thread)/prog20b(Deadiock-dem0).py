#  Find  outputs  (Home  work)
from  threading  import  *
import  time
def  f1(): #  Executed  by  thread  t1
	l1 . acquire() #  t1   locks  object  l1
	print('1st  thread  locks  object  l1')
	time . sleep(1)  #  t1   sleeps  for  1  sec
	l2 . acquire()  #  t1  waits  as object  l2  is  already  held  (or)  locked  by  t2
	print('1st  thread  is  under  execution')  #  Not  executed  due  to  infinite  wait
	l2 . release()
	l1 . release()
	print('End  of  the  1st  thread')
def  f2():  #  Executed  by  thread  t2
	l2 . acquire()  #  t2   locks  object  l2
	print('2nd   thread  locks  object  l2')
	time . sleep(1)  #  t2   sleeps  for  1  sec
	l1 . acquire()   #  t2  waits  as object  l1  is  already  held  (or)  locked  by  t1
	print('2nd   thread  is  under  execution')  #  Not  executed  due  to  infinite  wait
	l1 . release()
	l2 . release()
	print('End  of  the  2nd   thread')
# End  of  the  function
l1 = Lock()  #  Creates  two  Lock  objects
l2 = Lock()
t1 = Thread(target = f1)  #  Creates  two  threads
t2 = Thread(target = f2)
t1 . start() #  t1  executes  function  f1()
t2 . start()  #  t2  executes  function  f2()
time . sleep(1)  #  main  thread  sleeps  for  1  sec
print('Deadlock')  #  Deadlock




'''
1) Thread  t1  locks  object   l1  and  thread  t2  locks  object  l2

2) t1  fails  to  lock  object  l2  becoz  it  is  already  held  by  t2  and  hence  t1  waits  until  l2  is  unlocked

3) t2  fails  to  lock  object  l1  becoz  it   is  already  held  by  t1  and  hence  t2  waits  until  l1  is  unlocked

4) Finally,  each  thread  holds  an  object  and  waits  for  the  other  object

5) This  is  called  deadlock  and  no  thread  can  complete  execution  due  to  deadlock
'''
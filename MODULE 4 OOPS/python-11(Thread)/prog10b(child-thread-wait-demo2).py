# Find   outputs (Home  work)
from threading import *
import  time
def    disp():
	main_thread() . join(10)   #  child  thread  waits  for  10  sec  (or) expiry of  main  thread
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = disp) #  Creates  a  new  thread
child . start() #  child  thread  executes  disp()  function
for  i  in  range(10):
	print('main  thread')
	time . sleep(2)


'''
Sec  0:  main  thread
Sec  2:  main  thread
Sec  4:  main  thread
Sec  6:  main  thread
Sec  8:  main  thread
Sec  10:  Either  main  thread  (or)  10  times  child  thread
Sec  12:  Either  main  thread
Sec  14:  Either  main  thread
Sec  16:  Either  main  thread
Sec  18:  Either  main  thread
Sec  20:  Either  main  thread
'''


'''
1) What  are  the  outputs  if  it  is  time . sleep(3) ?  --->  4  times  main  thread
																					       10  times  child  thread
																					       6  times  main  thread
    Are  outputs  same  for  every  run ?  --->  Same  for  every  run

2) What  are  the  outputs  if  it  is  time . sleep(2.5) ?  ---> 4  times  main  thread
																							  main  thread  (or)  10  times  child  thread
																							  5  times  main  thread
     Are  outputs  same  for  every  run ?  --->  Vary  from  run  to  run  after  10th  sec

3) What  are  the  outputs  if  it  is  time . sleep(4) ?  --->  3  times  main  thread
																							10  times  child  thread
																							7  times  main  thread
     Are outputs  same  for  every  run ?  --->  Yes  becoz  only  child  thread  is  ready  for  execution  after  10th  sec
								                                       and  main  is  ready  for  execution  for  every  4  sec
																	   (and  10  is   not  a  multiple  of  4)
'''
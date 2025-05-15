#  Find  outputs  (Home  work)
from threading import *
import time
def  disp():
	main_thread() . join()     #  child  thread  waits  for  expiry  of  main  thread
	for  i  in  range(10):  #  Not   executed
		print('child  thread')
child = Thread(target = disp)  #  Creates  a   new  thread
child . start()  #  child  thread  executes  disp()  function
child . join()    #  main  thread  waits  for  expiry  of  child  thread
for  i  in  range(10):   #  Not   executed
	  print('main  thread')


'''
1) What  are  the  outputs ?  --->  No  outputs

2) main  thread  waits  for  child  thread  expiry  and  vice-versa

3) Neither  main  thread  finishes  execution  nor  child  thread

4) They  wait  for  each  other  and  leads  to  dead lock

5) Press  ctrl + break  or  Fn + B  to  suspend  deadlock
'''
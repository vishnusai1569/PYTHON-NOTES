# Find  outputs (Home  work)
from threading import *
def   disp():    #  Executed  by  child  thread
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = disp)
child . start()    # child  thread  executes  disp()  function
child . join()   #  main  thread  waits  for  expiry  of  child  thread
for  i  in  range(10):   #  Executed  after  child  thread  is  dead
	print('main  thread')


'''
1) What  is  main  thread  doing ?  --->  Creates  child   thread  ,  starts  child  thread  and  waits  for  child  thread  expiry

2) What  are  the  outputs ?  --->  10  times  child  thread
													  10  times  main  thread

3) Are  outputs  same  for  every  run  ? --->  Yes  inspite  of  having  multiple  threads
'''
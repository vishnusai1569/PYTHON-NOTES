#  Find  outputs (Home  work)
from  threading  import *
import  time
def   disp():
	for  i  in  range(10):
		print('child  thread')
		time . sleep(2.5)
child = Thread(target = disp)
child . start()
child . join(10)  #  main  thread  waits  for  10 sec  (or)  child  thread expiry  (whichever   happens  first)
for  i  in  range(10):
	print('main  thread')



'''
1) Are  outputs  same  for  every  run ?  --->  No  becoz  both  the  threads  are  ready  for  execution  at  10th  sec

2) However  outputs  are  same  for  first  10  sec  i.e.  5   times  child  thread

3) What  are  the  outputs  for  time . sleep(3) ?  --->   4 times  child  thread ,
																					   10  times  main  thread ,
																				       6  times  child  thread

4) Are  outputs  same  for  every  run  when  it  is  time . sleep(3) ?  --->  Yes
'''
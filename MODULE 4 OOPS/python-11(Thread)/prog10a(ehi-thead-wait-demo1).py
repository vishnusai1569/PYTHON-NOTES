'''
Modify  following  program  such  that  child  thread  should  wait  for  main  thread  expiry
(Home  work)
'''
from threading import *
def   disp(): #   It  is   executed  by  child  thread
	main_thread() . join() #     child  thread  waits  for  main  thread  expiry
	for  i  in  range(10):  #   Executed  soon  after  main  thread  is   dead
		print('child  thread')
child = Thread(target = disp)   #   A  new  threaad  is  created
child . start() # child  thread  executes  disp()  function
for  i  in  range(10):
	print('main  thread')


'''
10  times  main  thread
10  times  child  thread
'''

'''
1) child . join()
    What  is  the  issue  with  the  above  statement  in  disp()  function ?  --->
																				child  thread  waits  for  its  own  expiry  which  raises  an  error

2) In general,  a  thread  can  wait  for  expiry  of  different  thread  but  not  same  thread

3) current_thread() . join()
    What  is  the  issue  with  the  above  statement  in  disp()  function ?  --->
																	   child  thread  waits  for  its  own  expiry  which  raises  an  error
'''
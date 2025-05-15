# Recursive  function  for  n!
from  threading  import  *
import  time
def    fact(n):
	r . acquire()  #
	if   n > 0:
		x = n * fact(n - 1) #   x =
	else:
		x =  1
	r . release() #  pending  for  4th   time
	return   x
'''
Function  call     Thread locks  obj          Variable  'x'               Thread  unlocks  object       Where  is  x  returned to ?
                            'r'  for   ith  time                                             'r'   for   ith   time
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   fact(4)                  i = 1                         x = 4 * fact(3) = 4 * 6 = 24       i = 5                               fact(4)
   fact(3)                  i = 2                         x = 3 * fact(2)  = 3 * 2 = 6        i = 4                              fact(3)
   fact(2)                  i = 3                         x = 2 * fact(1) = 2 * 1 = 2          i = 3                              fact(2)
   fact(1)                  i = 4                          x = 1* fact(0) = 1 * 1 = 1            i = 2                             fact(1)
   fact(0)                 i = 5                           x = 1                                          i = 1                             fact(0)
'''
def    disp(n):
	print(F'{n}   !=  {fact(n)}')  #  t1  prints   4 != fact(4)  --->  4 != 24
t1 = Thread(target = disp , args = (4,)) #  Creates  2  new  threads
t2 = Thread(target = disp , args = (7,))
r = Lock() #  Object  is  created
t1 . start() #  t1  executes  disp(4)
t2 . start()  #  t2  executes  disp(7)



'''
What  happens  when  Lock  object  is  used  in  the  above  program ? --->
												1) t1  locks  object  'r'   for  the  function  call  fact(4)  and
													waits  for  fact(3)  becoz  it  can  not   be  locked  again
												2) t2  also  waits  becoz  object  is  already  locked  by  t1
												3) Both  t1  and  t2  wait  forever  and  hence  no  results
'''
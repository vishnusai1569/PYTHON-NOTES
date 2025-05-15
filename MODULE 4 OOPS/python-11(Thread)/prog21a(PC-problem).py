# Producer-Consumer  problem
from  threading  import  *
import  time
from  random  import  randint
class  Buffer:
	def   store(self , y):  # self  is   object  buf   and   'y'  is  2
		s = current_thread() . name  # Name  of  thread  'p'  i.e. 'Producer'
		self . x  =  y  #  Adds  variable  'x'  to  object  buf  with  value  'y'
		print(s  ,  'stores' ,  self . x)
	def   ret(self):  #  self  is  object   buf
		s = current_thread() . name  # Name  of  thread  'c'  i.e. 'Consumer'
		print(s  ,  'retrieves' ,  self . x)  #  Prints  buf.x
def   f1(buf):  #  Executed  by  thread  'p'
	i = 1
	while   True:  #  Iteration  2
		buf . store(i)  #  Stores  value  of   'i'  in  buf.x
		i += 1  #   Move  to  next  value
		time . sleep(randint(1 , 4)) #   Thread   'p'  sleeps  for  1  to  4  sec
def  f2(buf):
	while  True:  #  Iteration  2
		buf . ret()  #  Prints  buf.x
		time . sleep(randint(1 , 4))  #   Thread   'c'  sleeps  for  1  to  4  sec
buf = Buffer()   #   Empty  object
p  = Thread(target = f1 , name = 'Producer' , args = (buf,))  #  Creates  2  new  threads
c  = Thread(target = f2 , name = 'Consumer' , args = (buf,))
p . start()  # Thread  'p'  executes  f1(buf)
c . start()  # Thread  'c'  executes  f2(buf)
print('Press  ctrl + break  or  Fn+B  to  stop')
#  main  thread  is  dead


'''
1) What  does  main  thread  do  ?  --->  Creates  Buffer  object ,  creates  2  threads  and  starts  both  of  them

2) What  does  thread  'p'  do  ?  --->  Stores  a  value  in  the  buffer  object ,  sleeps  for  1  to  4  sec  and
														     repeats  this  process  for  infinite  number  of  times

3) What  does  thread   'c'  do ?  --->  Retrieves  value  from  buffer  object ,  sleeps  for  1  to  4  sec  and
															 repeats  this  process  for  infinite  number  of  times

4) What  are  the  three  issues  with  the  above  program ?  --->
	 a) Consumer  thread  retrieves  same  value  repeatedly  when  producer  thread  sleeps  for  longer  time
	 b) Consumer  thread  miss  some  of  the  values  when  consumer  thread  sleeps  for  longer  time,
	 c) buf . x  throws  error  when consumer  thread  is  first  started  becoz  there  is  no  variable  'x'  in  object   buf

5) Is  it  possible  to  overcome  the  above  issues  with  time . sleep(1) ?  --->
											No  becoz  we  have  no  idea  which  thread  will  get  the  chance  after  1  sec
'''
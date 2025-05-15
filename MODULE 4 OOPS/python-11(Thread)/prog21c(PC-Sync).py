'''
Producer-Consumer  problem  with  synchronization

1) Add  one  more  variable  to  buffer  object  i.e.  write  variable

2) What  does  write = True  indicate ?  --->  Thread  'p'  can  write  a  value  to  the  buffer  object
    What  does  write = False  indicate ?  --->  Thread  'p'  can  not  write  a  value  to  the  buffer  object

3) Initialize  write  = True  in  the  constructor  of  buffer  class

4) What  are  the  four  events  for  thread  'p' ?  --->  a) Write  a  value  to  buf . x  when  buf . write = True
     b) Modify  buf . write = False  becoz  thread  'p'  can  not  write  another  value  to  object  buf   immediately
	 c) Notify  thread  'c'  that  a  new  value  is  available  in  object   buf
	 d) Thread  'p'  waits  due  to   buf . write = False

5) What  are  the  four  events  for  thread  'c' ?  --->  a) Prints  buf . x  when  buf . write = False
	 b) Modify  buf . write = True  becoz  thread  'c'  can  not  print  same  buf . x  again
	 c) Notify  thread  'p'  that  value  is  retrieved  from  object   buf
	 d) Thread  'c'  waits  due  to  buf . write = True

6) Modify  store()  and  ret()  methods  as  indicated  above
    and  also  add  constructor  to  buffer  class

7) Functions  f1() , f2()  and  the  code  outside  remains  same
'''
from  threading  import  *
import   time
from  random  import  *
class   Buffer:
	def   __init__(self):   #  self  is  object  buf
		self . write = True   #   Adds  variable  write  to  object   buf  with  value  True
	def   store(self , y): #   self  is  object buf  and   'y'  is  value  of  'i'
		cond . acquire()   #  Thread  'p'  locks   cond  object  (mandatory  before  calling  wait())
		if   not  self . write:
			cond . wait()  #   Thread  'p'  waits  when  buf . write  =  False
		s = current_thread() . name  #   Name  of   thread  'p'   i.e.  "Producer"
		self . x  =  y  #  Writes  value  to  buf . x
		print(s  , 'Stores'  ,  self . x)  #   Producer  stores  some  value
		self . write = False   #  Thread  'p'  can  not  write  next  value  immediately
		cond . notify()  #   Thread  'p'  notifies  the  first  waiting  thread  i.e. Thread  'c'
		cond . release()  #   Thread  'p'  unlocks  cond  object
	def   ret(self):   #  self  is  object  buf
		cond . acquire()   #  Thread  'c'  locks   cond  object  (mandatory  before  calling  wait())
		if   self . write:
			cond . wait()    #   Thread  'c'  waits  when  buf . write  =  True
		s = current_thread() . name  #   Name  of   thread  'c'   i.e.  "Consumer"
		print(s  , 'Retrieves' , self . x)  #   Consumer  retrieved  some  value
		self . write = True    #  Thread  'c'  can  not   retrieve  same   value  again
		cond . notify()  #   Thread  'c'  notifies  the  first  waiting  thread  i.e. Thread  'p'
		cond . release()   #   Thread  'c'  unlocks  cond  object
def   f1():  #  Same  as    prog21a
	i = 1
	while  True:
		buf . store(i)
		i += 1
		time . sleep(1)
def   f2():  #  Same  as    prog21a
	while  True:
		buf . ret()
		time . sleep(1)
#  Following  statements  are  same  as  prog21a
cond = Condition()
buf = Buffer()
p  = Thread(target = f1 , name = 'Producer')
c  = Thread(target = f2 , name = 'Consumer')
c . start()
p . start()
print('Press  ctrl+break  or    Fn+b  to  stop')


# object   buf   --->  write = True , x  = 1
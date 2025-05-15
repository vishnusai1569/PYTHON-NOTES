# Find  outputs (Home  work)
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('Child  Thread')
child = MyThread()
child . start() #  child  thread  executes  empty run method  of  Thread  class  as  there  is  no  run()  method  in  MyThread  class
for  i  in  range(10):
	print('Main  Thread')  #  Main  Thread  10 times



'''
1) When  is  walk()  mehod  executed ?  --->   As  soon  as  it  is  called  explicitly  by  child . walk()
																					       (or)
																       send  target = MyThread() . walk  to  the  constructor
																	   i.e. child = MyThread(MyThread() . walk)

2) What  about  run()  method ?  --->  It  is  automatically  executed  as  soon  as  thread  is  started
'''
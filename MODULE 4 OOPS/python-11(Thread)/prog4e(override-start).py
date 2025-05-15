#  What  are  the  outputs  when  start()  method  is  overridden  ?  (Home  work)
from  threading  import  *
class  MyThread(Thread):
	def   start(self):
		super() . start() #  start method of Thread class  registers  child  thread   with  TS
		print('Start Method')
	def   run(self):
		print('Run Method')
#  main  thread  executes  following  statements
child = MyThread()
child . start() #  Method  call  to  start method of MyThread class
print('Main  Thread')

'''
Run Method
Start Method
Main  Thread
'''


'''
1) Which  class  start()  method  is  executed  for  child . start() ? --->
																start()  method  of  MyThread  class  becoz  child  is  MyThread  class  object

2) Which  class  start()  method  is  executed  for  super() . start() ?  --->
												start()  method  of  Thread  class  becoz  super()  refers  to  parent  class  Thread

3) Is  child . start()  a  method  call  (or)  thread  register  ?  --->
																			Method  call  becoz  it  is  start()  method  of  MyThread  class

4) Is  super() . start()  a  method  call  (or)  thread  register ?  --->
																				Thread  register  becoz  it  is  start()  method  of  Thread  class

5) Which  thread  is  executing  start()  method  of  MyThread  class ?  --->  main  thread  becoz  it  is  called  by   main  thread

6) Which  thread  is  executing  run()  method  of  MyThread  class?  --->   Child  thread
'''
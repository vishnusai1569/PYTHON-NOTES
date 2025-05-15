# How  to  implement  a  thread   with  run()  method
from  threading  import  *
class  MyThread(Thread):
	def  run(self):   #  Executed  by   child  thread
		for   i  in   range(1 ,  11):
			print('child  thread  :  ' ,  i)
#  main  thread  executes  folllowing  statements
child = MyThread()  #  Creates  a new  thread   (default  target  is  run()  method  of  MyThread  class)
child . start() #  child  thread  executes  run()  method  of  MyThread  class
for  i  in  range(1 , 11):
        print('main  thread  :  ' , i)


'''
1) Is  MyThread  a  thread ?   --->  Yes  becoz  it  is  a  child  class  of  Thread

2) child = MyThread()
     child . start()
     Which  class  start()  method  is  executed   ?  --->  start()  method  of  Thread  class  is  executed  becoz
																				       there  is  no  start()  method  in  MyThread  class

3) What  does  start()  method  of  Thread  class  do ?  --->  Registers  child  thread  with  thread  scheduler

4) What  does  child  thread  do ?  --->  Executes  run()  method  of  MyThread  class  becoz  child  is  MyThread  class  object

5) Can  method  name  be  walk() ?  --->  No  and  it  should  be  run()  only
'''
# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function')
child = MyThread(target = f1)
child . start()   #  child  thread  executes  run()  method  of  MyThread  class  and  ignores  target
print('Main  Thread')

'''
run  method
Main  Thread
'''

'''
1) Which  method  has  got  highest  priority ?  --->  run()  method  of  same  class

2) Which  method  has  got  2nd  highest  priority ?  --->  target  function  (or)  method

3) Which  method  has  got  lowest  priority ?  --->  Empty  run()  method  of  Thread  class
'''
# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for  i  in   range(1 , 11):
		print('f1  function : ' , i)
child = MyThread(target = f1)
child . start()   #  child  thread  executes  target (i.e. f1  function)  becoz  there is  no   run()  method   in  MyThread  class
for  i  in  range(1 , 11):
	print('Main  Thread : ' , i)
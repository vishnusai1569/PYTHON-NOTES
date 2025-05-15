# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start() #  child  thread  executes  empty run() method  of  Thread  class
print('Main  Thread')   #  Main  Thread
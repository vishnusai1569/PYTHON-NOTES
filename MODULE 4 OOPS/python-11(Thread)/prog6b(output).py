# Find  outputs (Home  work)
from  threading  import  *
def  f1():
	print(current_thread() . name) # How  to  print  name  of  child  thread
child = Thread(name = 'Child', target = f1) # How  to  create  a  new  thread  with  name  "Child"  and  target  f1
child . start() # How  to  start  the  new  thread
print(main_thread() . name) # How  to  print  name  of   main  thread

'''
Child
MainThread
'''
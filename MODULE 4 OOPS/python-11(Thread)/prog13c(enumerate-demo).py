# Find  outputs  (Home  work)
from  threading  import  *
import  time
def   disp():
	name = current_thread() . name
	print(name , ' is  started')
	time . sleep(3)
	print(name , '  is  ended')
t1 = Thread(target = disp , name = 'One')   #  Creates  3  new threads
t2 = Thread(target = disp , name = 'Two')
t3 = Thread(target = disp , name = 'Three')
t1 . start() #  t1  executes  disp()  function
t2 . start() #  t2  executes  disp()  function
t3 . start()  #  t3  executes  disp()  function
list = enumerate()  #   Returns  a  list  of  all  the  thread  i.e. [main , t1 , t2 , t3]
for  t  in   list:  #  't'  is  each thread  of  the  list
	print(t . name)#   Name  of  each  thread  in  the  list
t1 . join() #  main  thread  waits  for  expiry  of  t1 , t2  and t3
t2 . join()
t3 . join()
list = enumerate()  #   Returns  a  list  of   single  thread (i.e. main  thread) as  t1 , t2  and  t3  are  dead  i.e. [main]
for  t  in  list:  #  Executed  just  once  as  list  has  single  thread  main
	print(t . name) #  Name  of  main  thread  i.e.  MainThread



'''
One is  started
Two is  started
Three is  started
MainThread
One
Two
Three
One is  ended
Two is  ended
Three is   ended
MainThread
'''
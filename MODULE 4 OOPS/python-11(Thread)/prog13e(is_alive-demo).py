# is_alive()  method   demo  program
from  threading  import *
import  time
def   disp():
	name =  current_thread() . name
	print(name , 'is   started')
	time . sleep(3)
	print(name , '   is    ended')
t1 = Thread(target = disp , name = 'One')   #  Creates 3  new threads
t2 = Thread(target = disp , name = 'Two')
t3 = Thread(target = disp , name = 'Three')
t1 . start() #  t1  executes  disp()  function
t2 . start()  #  t2  executes  disp()  function
t3 . start()  # t3  executes  disp()  function
print(t1 . is_alive())  # True :  t1  is  alive  as   it  is  sleeping
print(t2 . is_alive())  # True :  t2  is  alive  as   it  is  sleeping
print(t3 . is_alive())  # True :  t3   is  alive  as   it  is  sleeping
t1 . join() #  main  thread  waits  for  expiry  of  t1 , t2  and t3
t2 . join()
t3 . join()
print(t1 . is_alive()) #  False : t1  is  dead
print(t2 . is_alive())  #  False : t2  is  dead
print(t3 . is_alive())  #  False : t3  is  dead

'''
One is   started
Two is   started
Three is   started
True
True
True
One   is   ended
Two   is   ended
Three   is   ended
False
False
False
'''

#  active_count() ,  enumerate()  and  is_alive()  are  almost  same
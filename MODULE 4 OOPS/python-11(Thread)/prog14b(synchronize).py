# Repeat  prog14a  with  synchronization
from  threading  import  Lock , Thread
import  time
def   table(n):
	l . acquire() #   t1  locks  object   'l'
	print('Table  :  ' , n)
	for  i  in  range(1 , 11):
		print(F'{n}  *  {i}  =   {n * i}')
		time . sleep(1)
	l . release() #  t1  unlocks  'l'
#  t1  is  dead
t1 = Thread(target = table , args = (7,))
t2 = Thread(target = table , args = (4,))
l = Lock()  #  Creates  Lock  class  object
t1 . start()  #  t1  executes  table(7)
t2 . start()   #  t2  executes  table(4)
#  main  thread   is  dead


'''
1) Threads  t1  and  t2  try  to  execute  table()  function  concurrently  but  it  is  denied  due  to  locking  mechanism

2) Therefore  they  are  forced  to  execute  table()  function  serially

3) Synchronization  is  achieved  and  accurate  results  are  obtained

4) What  happens  if  t1  does  not  unlock  object  'l' ?  --->  t2   waits  forever

5) Hence  unlock  is  mandatory
'''
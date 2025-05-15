# Find  outputs (Home  work)
from  threading  import  *
import  time
def   table(n):
	print('Table  :  ' , n)
	for i  in  range(1 , 11):
		print(F'{n}  *  {i}    =   {n * i}')
		time . sleep(1)
t1 = Thread(target = table , args = (7,))
t2 = Thread(target = table , args = (4,))
t1 . start()  #  t1  executes  table(7)
t2 . start()  #  t2  executes  table(4)
# main  thread  is  dead


'''
1) table()  function  is  being  executed  by   t1  and  t2  concurrently  and  hence  incorrect  results

2) Use  locking  mechanism  to  avoid  concurrent  execution
'''
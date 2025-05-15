# Find  outputs (Home  work)
from  threading  import *
import  time
def   disp(s):  # Executed  by  t1 , t2  and  t3 concurrently
	print('[' , s , end = '')
	time . sleep(3)
	print(']')
t1 = Thread(target = disp , args = ('Hyd',))  # Creates  3  new  threads
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1 . start() # t1 executes disp('Hyd')
t2 . start() # t2 executes disp('Sec')
t3 . start() # t3 executes disp('Cyb')

'''
[Hyd[Sec[Cyb]
]
]
'''


'''
1) t1  prints  [Hyd  and  sleeps  for  3  sec

2) t2  prints  [Sec  and  sleeps  for  3  sec

3) t3  prints  [Cyb  and  sleeps  for  3  sec

4) All  the  3  threads  are  ready  for  execution  after  3  sec

5) Can  outputs  be predicted  after  3  sec ?  --->
										No  becoz  we  have  no  idea  in  what  order TS  picks  the  threads  after  3  sec

6) Are  outputs  synchronized ?  --->  No  becoz   disp()  function  is  executed  concurrently  by  all  the  3  threads
'''
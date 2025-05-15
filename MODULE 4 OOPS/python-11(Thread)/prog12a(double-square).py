# Find  outputs (Home  work)
from threading import *
import time
def   double():
	for   i  in  range(1 , 7):
		print('Double : ' , 2 * i)
		time . sleep(1)
def   square():
	for   i  in   range(1 , 7):
		print('Square : ' , i * i)
		time . sleep(1)
start = time . time()  #  Current  time  before  execution  of   double()  and  square()  functions
double() # 6 seconds
square() # 6 seconds
end = time . time()    #  Current  time   after   execution  of   double()  and  square()  functions
print('Execution  time  of  the  two  functions : ' , end - start)  #  12.something

'''
Double : 2
<After  2  sec>
Double : 4
<After  2  sec>
Double : 6
<After  2  sec>
Double : 8
<After  2  sec>
Double : 10
<After  2  sec>
Double : 12
<After  2  sec>
Square : 1
<After  2  sec>
Square : 4
<After  2  sec>
Square : 9
<After  2  sec>
Square : 16
<After  2  sec>
Square : 25
<After  2  sec>
Square : 36
<After  2  sec>
Execution  time  of  2 functions : 12.something
'''


'''
1) How  many  threads  are  in  the  program ? --->  1  i.e.  main  thread

2) Who  is  executing  double()  and  square()  functions ? --->  main  thread

3) Are   double()  and  square()  functions  executed  concurrently  (or)  serially ? --->
										Serially  becoz  both  the  functions  are  being  executed  by  same  thread  i.e.  main  thread
'''
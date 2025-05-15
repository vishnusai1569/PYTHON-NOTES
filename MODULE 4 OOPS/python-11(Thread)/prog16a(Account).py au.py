#  Find  outputs (Home  work)
from  threading  import *
import  time
class   Account:
	def    __init__(self , acno1 , bal1):
		self . acno = acno1
		self . bal = bal1
	def    credit(self , amt): #  Executed  by   t1  and  t2  concurrently
		s = current_thread() . name  #  Name  of  the  thread  which  is  under  execution
		print(F'{s}  is  depositing  Rs. {amt}  into account   {self . acno}')
		x = self . bal #  Copy  balance to  local  variable  'x'
		time . sleep(1)
		self . bal  =  x  +  amt #  Balance  is  updated
ac = Account(25 , 1000.0) #  Object  is  initialized  with  acno = 25 , bal = 1000.0  by  constructor
print('Initial  Balance :  ' , ac . bal)  #  Initial  Balance :  1000.0
t1 = Thread(target = ac . credit ,  args = [100] ,  name = 'Rama') #  Creates  2  new  threads  t1  and  t2
t2 = Thread(target = ac  . credit , args = (200,) , name = 'Sita')
t1 . start() # t1 executes ac . credit(100)
t2 . start() # t2 executes ac . credit(200)
t1 . join() #  main  thread  waits  for  t1  and  t2 expiry
t2 . join()
print('Final  Balance  :   ' , ac . bal)  #  Final  Balance  :   1100.0   (or)  1200.0  but  not  1300.0

'''
Initial  Balance :  1000.0
Rama  is  depositing  Rs. 100  into account   25
Sita  is  depositing  Rs. 200  into account   25
(if  t1  resumes  first  after  1  sec)
Final  Balance  :   1200.0
(or)
(if  t2  resumes  first  after  1  sec)
Final  Balance  :   1100.0
'''



'''
1) t1  copies  Rs.1000  to  local  variable  'x'  and  sleeps

2) t2  also  copies  Rs.1000  to  another  local  variable  'x'  and  sleeps

3) Case  1:   t1  writes  Rs.1100  to  ac . bal  replacing  1000  after  1  sec  and
                   t2  writes  Rs.1200  to  ac . bal  replacing   1100
			       Final  bal  is   1200

    Case  2:   t2  writes  Rs.1200  to  ac . bal  replacing  1000  after  1  sec  and
                   t1   writes  Rs.1100  to  ac . bal  replacing   1200
  			       Final  bal  is   1100

4) Final  balance  is  either  1100  or  1200  but  not  1300  becoz  locking  mechanism  is  not  used

5) What  is  the  final  balance  if  t1 . join()  and   t2 . join()  are  omitted ?  --->  1000
'''
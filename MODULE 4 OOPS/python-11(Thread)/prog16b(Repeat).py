#  Modify  following  program  such  that  final  balance  should  be  1300
from  threading  import  *
import  time
class   Account:
	def  __init__(self , acno1 , bal1):
		self . acno = acno1
		self . bal = bal1
	def  credit(self , amt):
		l . acquire()
		s = current_thread() . name
		print(F'{s}  is  depositing  Rs. {amt}   into  account   {ac . acno}')
		x = self . bal
		time . sleep(1)
		self . bal = x + amt
		l . release()
ac = Account( 25 , 1000.0)
l = Lock()
print('Initial  Balance :  ' , ac . bal )
t1 = Thread(target = ac . credit , name = 'Rama' , args = (100,))
t2 = Thread(target = ac . credit , name = 'Sita' , args = (200,))
t1 . start()
t2 . start()
t1 . join()
t2 . join()
print('Final balance :  ' , ac . bal)


#  object   ac   --->  acno  =  25 , bal  =  1300.0


'''
1) t1  locks  object  'l' ,  copies  Rs.1000  to  local  variable 'x'  and  sleeps

2) t2  is  unable  to  lock  object  'l'  becoz  it  is  already  locked  by  t1  and
    hence  t2  waits  until  object 'l'  is  unlocked

3) t1  writes  Rs.1100  to  ac . bal  replacing  1000, unlocks  object  'l'  and  dead

4) t2  locks  object  'l' ,  copies  Rs.1100  to  local  variable 'x'  and  sleeps

5) t2  writes  Rs.1300  to  ac . bal  replacing  1100 , unlocks  object 'l' and  dead

6) main  thread  prints  final  balance (i.e. Rs. 1300)  after  t1  and  t2  are  dead

7) t1  and  t2  try  to  execute  credit()  method  concurrently  but
     it  is  denied  due  to  locking  mechansim

8) Every thread should follow:
     a) lock  object  'l'
     b) execute  statements  of  credit()  method
     c) unlock object  'l'

9) Accurate  results  are  obtained  due  to  serial  execution
'''
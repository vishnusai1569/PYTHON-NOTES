# How  to  implement  a  thread  with  method
from  threading  import  Thread
class   c1:
	def  m1(self):   #  Executed  by  child  thread
		for  i  in  range(1 , 11):
			print('Child  Thread' , i)
# main  thread  executes all  the  following  statements
a = c1()  #  Object
child = Thread(target = a . m1)  #  Creates a  new  thread
child . start()  # child  thread  executes  m1()  method  of  class  c1
for  i  in  range(1 , 11):
        print('Main  Thread' , i)



'''
1) child = Thread(target = m1)
    Is  the  statement  valid ?  ---> No  becoz  function  m1()  does  not  exist

2) child = Thread(target = c1 . m1)
    Is  the  statement  valid ?  --->  No  becoz   m1  is  neither  a  static  method  nor  a   class  method  of  class  c1

3) child = Thread(target = c1() . m1)
    Is  the  statement  valid ?  ---> Yes  m1()  is  an  instance  method  of  class  c1
'''
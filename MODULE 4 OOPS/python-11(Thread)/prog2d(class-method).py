#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(target = c1 . m1)
child . start()   #  child  thread   executes  class   method  m1   of  class  c1
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)


'''
1) Is  target =  c1() . m1  valid ?  --->  Yes  but  not  recommended  becoz  m1  is  a  class  method 

2) Can  outputs  of  the  program  be  predicted ?  --->  No  due  to  multiple  threads

3) In  other  words,  outputs  vary  from  run  to  run
'''
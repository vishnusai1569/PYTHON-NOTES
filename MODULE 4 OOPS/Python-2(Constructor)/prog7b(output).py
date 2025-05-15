

#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)  #  Two  argument  constructor :  <space>  10  <space>  20
b = c1(30)   #  Error :  Arg is  not  passed  for  'y'  of  the  constructor
c = c1()  #  Error :  Args  are  not  passed  for  'x'  and  'y'  of  the  constructor
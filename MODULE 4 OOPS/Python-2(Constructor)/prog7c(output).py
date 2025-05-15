prog7c(output).py

#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)  #  Two  argument  constructor :  <space>  10  <space>  20
b = c1(30)  #  Two  argument  constructor :  <space>  30  <space>  200
c = c1()  #  Two  argument  constructor :  <space>  100  <space>  200
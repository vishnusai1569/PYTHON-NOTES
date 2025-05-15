#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)  #  child method  --->  x :  10  <tab>  y : 20
c . m1(30 , 40)   #  child method  --->  x :  30  <tab>  y : 40


'''
parent  class  method  is  ignored  becoz  it  is  overridden  by  child  class
'''
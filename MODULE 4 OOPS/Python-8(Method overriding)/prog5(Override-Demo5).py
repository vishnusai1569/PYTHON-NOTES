# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		print('parent  method')
		return  x + y
class  child(parent):
	def   add(self , x , y , z = 3):
		print('child  method')
		return  x + y + z
#end of the class
c = child()
print(c . add(10 , 20 , 30))  #  Executes  method  of  child  class  and  result  is   60
print(c . add(10 , 20))  #  Executes  method  of  child  class  with  default  value  for  'z'  and  result  is   33


'''
child  method
60
child  method
33
'''
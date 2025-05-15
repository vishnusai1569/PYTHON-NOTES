# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):  #  Not  inherited  becoz  there  is  already  add() method  in  child  class
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return  x + y + z
#end of the class
c = child()
print(c . add(10 , 20 , 30)) # Executes  method  of  child  class  and  result  is   60
#print(c . add(10 , 20))  #   Error :  Arg  is  not  passed  for  'z'  of  child  class  method


'''
1) Is  add()  method  of  child  class  a  overriding  method ?  --->
											Yes  becoz  method  name  is  same  even  though  number  of  arguments   are  different

2) Is  add()  method  of  parent  class  inherited  to  child  class ?  --->
																					No  becoz  it  is  overridden  by  child  class
'''
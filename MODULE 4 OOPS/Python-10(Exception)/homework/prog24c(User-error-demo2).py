# Find  outputs   (Home  work)
class   MyError(NameError):
	def    __init__(self): #  self   is  MyError  object
		self . a =  25  #  self . a = 25
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)
	if  x > 20:
		raise   MyError()  #  Object is  initialized  with  a  = 25  by  constructor  and  is  passed  to  except  suite
	print('Hello')
#end of  the functrion
try:
	compute(30) #  30  <next  line>  Constructor  <next  line>
	compute(10)   #  Skipped  :  MyError  is  not yet   caught
except  MyError  as  msg: #   msg  is  empty string  :  There  is  no  arg  to  constructor  of MyError  class
	print('Caught  MyError  outside  :  ' ,  msg)  #  Caught  MyError  outside  :  <Nothing>
print('End')  # End
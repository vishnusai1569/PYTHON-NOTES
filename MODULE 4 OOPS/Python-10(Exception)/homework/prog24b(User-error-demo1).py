# Find  outputs   (Home  work)
class   MyError(BaseException):
	def    __init__(self , y):  #  self  is  MyError  object  ,   'y'  is   30
		self . a = y # self . a = 30
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)
	if  x > 20:
		raise   MyError(x)   # Object is initialized  with  a = 30  by  constructor  and   is   passed   except  suite
	print('Hello')
# End of  the functrion
try:
	compute(10) #   10 <next  line>  Hello  <next  line>
	compute(30)  #   30 <next  line>  Constructor  <next  line>
except  MyError  as  msg: #  msg is   value  of  MyError  object  i.e.  30
	print('Caught  MyError  outside  :  ' ,  msg)  #   Caught  MyError  outside  :  30
print('End')  # End




'''
raise  MyError(x)
What  are  the  three  events  in  execution  of  the  above  statement ?  --->
1) Creates  MyError  class  object
2) Initializes  object  with  value  of  x  by  constructor
3) Passes  object  to  except  suite
'''
#  Gift
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1()  #   Executes  constructor
	print(a)  #  __str__()  method  of   object  class  returns  type  and  address  of object  'a'
	print('Function  end')
	return   a
# Object  'a'  is   not  lost  becoz  ref  'b'  points to  the  object
print('Program  Begin')
b = f1() #   b = a  --->  'b'  points to  object  'a'  which  is  created  by  f1()  function
print(b)   #  __str__()  method  of   object  class  returns  type  and  address  of object  'a'
print('Program  End')
#Destructor  is  executed  before  object  'b'  is  lost



'''
Program Begin
Function Begin
Object is created
Type  and  address  of  object  'a'
Function End
Type  and  address  of  object  'a'
Program End
Object is Lost
'''


'''
1) Why  is  object  'a'  not  lost  after  f1()  function  terminates ?  --->  Since  reference  'b'  points  to  object   'a'

2) When  is  object  'a'  lost ?  --->  As  soon  as  program  terminates  becoz  there  is  no  reference
'''
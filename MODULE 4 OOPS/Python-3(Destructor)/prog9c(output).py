# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()  #  Executes  constructor
        print('Function  end')
# Executes  destructor  before  object  'a'  is  lost
print('Program  Begin')
b = f1()   #  Function  returns  None  by  default
print(b)
print('Program  End')

'''
Program Begin
Function Begin
Object is created
Function End
Object  is  lost
None
Program End
'''


'''
1) When  is  object  'a'  lost ?  --->  As  soon  as  f1()  function  terminates

2) Why  is  object  'a'   lost  after  f1()  function  terminates ?  --->  Since  it   is  not  returned   by  f1()  function
'''
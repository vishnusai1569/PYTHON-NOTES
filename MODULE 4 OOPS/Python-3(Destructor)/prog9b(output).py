#  Gift
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
        return   a   #  Object  'a'  is   returned  to  function  call  f1()
#  Executes  destructor  before  object  'a'  is  lost
print('Program  Begin')
f1()
print('Program  End')

'''
Program Begin
Function Begin
Object  is    created
Function End
Object is Lost
Program End
'''


'''
1) When  is  object  'a'  lost ?  ---> As  soon  as  f1()  function  terminates

2) Why  is  object  'a'   lost  after  f1()  function  terminates ?  --->  Since  there  is  no  reference  to  the  object
'''
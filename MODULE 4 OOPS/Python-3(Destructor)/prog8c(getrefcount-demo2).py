# Find  outputs  (Home  work)
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test() #  Executes constructor  and  ignores  None
print(t . __init__())  #  Executes constructor  ands  prints  None
print(sys . getrefcount(t))  #  Number  of  references  to  object  't'  i.e. 1 + 1   = 2
print(t . __del__())  #  Executes  destructor  and  prints  25
print(sys . getrefcount(t))   #  Number  of  references  to  object  't'  i.e. 1 + 1   = 2
print('Bye')
# Destructor  is  executed  before  object  't'  is  lost

'''
Constructor : address of  object  't'
Constructor : address of  object  't'
None
2
Destructor : address of  object  't'
25
2
Bye
Destructor : address of  object  't'
'''


'''
Is  object  lost  after  execution  of  destructor  ?  --->  No  when  it  is  called  explicitly  and
  																					      yes  when  it  is  automatically  executed
'''
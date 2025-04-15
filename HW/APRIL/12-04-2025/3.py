#  Gift
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1()
	print(a)
	print('Function  end')
	return   a
print('Program  Begin')
b = f1()
print(b)
print('Program  End')



"""
Program  Begin
Function  Begin
<__main__.c1 object at 0x1025de900>
Function  end
<__main__.c1 object at 0x1025de900>
Program  End
"""



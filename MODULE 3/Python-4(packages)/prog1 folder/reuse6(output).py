''' (Home work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
from  p1 . mod1    import    *
from  p1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x) #   Variable  of  same  module  i.e.  30
f1() #   Executes  function  of  same  module
a = c1()  #  Creates  c1  class   object  of  same  module
a . m1() #  Executes  method  of  class  c1  in same  module

'''
30
Function  of  same  module
Method  of  class  c1  in same  module
'''
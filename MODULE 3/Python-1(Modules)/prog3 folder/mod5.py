mod5.py

# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) #  Variable  of  same  module
disp() #   Function of  same  module
a = c1()  #  Creates  c1  class object  of  same  module
a . m1() # executes m1() method  of  class  c1  of  same  module

'''
30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''
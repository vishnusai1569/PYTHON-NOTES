
# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   * #  Modifies  variable  'x'  to  20
from  mod1  import   * #  Modifies  variable  'x'  to  10
print(x) #  Variable  'x'  os  mod1
disp() #   Executes  function  of  mod1
a = c1() #  Creates  mod1 . c1  class  object  becoz  it  is  imported  last
a . m1() # Executes  method  of  mod1 . c1

'''
10
disp  function  of  mod1
'm1  method  of  class  c1  in  mod1
'''


'''
Members  of  last  imported  module (i.e.  mod1)  are  used
'''
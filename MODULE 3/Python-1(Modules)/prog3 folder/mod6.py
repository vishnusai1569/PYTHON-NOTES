
# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1 , mod2  #How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1 . x) # How  to  print  variable  'x'  of  mod1
mod1.disp() # How  to  call  disp()  function  of  mod1
a = mod1 . c1()
a . m1()  #How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(mod2 . x) # How  to  print  variable  'x'  of  mod2
mod2.disp() # How  to  call  disp()  function  of  mod2
b = mod2 . c1()
b .  m1()   #How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(x) # How  to  print  variable  'x'  of  current  module)
disp() # How  to  call  disp()  function  of current  module
d = c1()
d . m1()  #How  to  call  method  m1()  of  class   c1  in  current  module




'''
10
disp  function  of  mod1
m1  method  of  class  c1  in  mod1
20
disp  function  of  mod2
m1  method of  class  c1  in  mod2
30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''
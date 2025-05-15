# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as v , disp as disp1 , c1 as c11  #How  to  import  members  of  mod1
from mod2 import x as u , disp as disp2 , c1 as c12  #How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(v) # How  to  print  variable  'x'  of  mod1)
disp1() # How  to  call  disp()  function  of  mod1
a = c11()
a . m1()  # How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(u) # How  to  print  variable  'x'  of  mod2)
disp2() # How  to  call  disp()  function  of  mod2
b = c12()
b . m1()  #How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(x) # How  to  print  variable  'x'  of  current  module)
disp()# How  to  call  disp()  function  of current  module
c = c1()
c . m1()  # How  to  call  method  m1()  of  class   c1  in  current  module



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
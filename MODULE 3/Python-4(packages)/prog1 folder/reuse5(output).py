'''  (Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod2    import   *
from  p1 . mod1    import   *
print(x) #  variable  'x'  of  p1 . mod1
f1() #  Executes  function  of   p1 . mod1
a = c1()  #  Creates  p1 . mod1 . c1  class  object
a . m1()    #  Executes   method  of   p1 . mod1 . c1  class

'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
'''
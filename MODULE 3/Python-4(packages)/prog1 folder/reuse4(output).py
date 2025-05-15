'''
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod1    import    *
from  p1 . mod2    import    *
print(x) #   Variable  'x'   of  p1 . mod2
f1() #   Function  of  p1 . mod2  is  executed
a = c1()  # Creates  p1 . mod2 .  c1  class  object
a . m1() #  Executes p1 . mod2 . c1 . m1()  method

'''
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1
'''


'''
Which  members  are  used  and  why ?  --->  Members  of  p1 . mod2  are  used  becoz  they  are  imported  last
'''
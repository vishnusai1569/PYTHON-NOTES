#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x  #  Treats  'x'  as  GV
		nonlocal  x  #  Error  :  'x'  is already  global  and  hence  can  not  be treated  as  variable  of  outer()  function


'''
Inner  function  can  use  either  nonlocal  keyword  (or)  global  keyword  but  not  both  simultaneously
'''

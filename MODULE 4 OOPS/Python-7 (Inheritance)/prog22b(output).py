# Find  outputs
class  parent:
	x = 10
	def  __init__(self):
		self . x = 20
class   child(parent):
	def  __init__(self):
		self . x = 30
		print(self . x)
		super() . __init__()
	def  disp(self):
		print(self . x)
		print(super() . x)
# End of the class
c = child() #  object  is  initialized  with  x = 30  and  modified  to  x = 20  by  child   and  parent  constructors
c . disp()

'''
30
20
10

static  variable  ---> x = 10

object  'c'  --->  Initially  x = 30  and  then  modified  to  x = 20
'''
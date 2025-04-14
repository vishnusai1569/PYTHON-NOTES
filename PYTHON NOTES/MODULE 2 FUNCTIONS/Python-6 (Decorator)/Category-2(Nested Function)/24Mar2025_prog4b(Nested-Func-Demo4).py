# Find  outputs  (Home   work)
x = 10  # Global  variable
def  outer():
	x = 20  #  Local  variable  of  outer()  function
	def   inner():
		print(x)  #  Local  variable  of  outer()  function  i.e.  20
		print(globals()['x'])  #  Gv  i.e.  10
	inner()
outer()





'''
When  can  inner  function  access  variable  of  outer()  function ?  --->
																When  there  is  no  LV  with  same  name  in  inner()  function
'''

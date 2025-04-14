# Find  outputs  (Home  work)
x = 10  # Gv
def  outer():
	def   inner():
		print(x)  #  Gv  i.e.  10
	inner()  #  Executes  inner()  function
outer()  #  Executes  outer()  function



'''
1) When  can  inner  function  access  global  variable  ?  --->
																			When  there  is  no  LV  in  inner()  and  outer()  functions

2) What  is  the  order  of  search  for  a  variable ?  --->  inner  function , outer  function  and  Gv
'''

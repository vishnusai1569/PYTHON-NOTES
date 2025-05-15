# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x  #  Treats  'x'  as  Gv
		x = 20 #  Creates  Gv  with  value  20
		print(x)#  Gv i.e.  20
		x = x + 5  #  Modifies  Gv   to  25
	# End  of  inner  function
	inner()
	print(x) # Gv  i.e.  25
# End  of  the  function
outer()
print(x)  # Gv  i.e.  25


'''
20
25
25



1) def  f1():
	   global  x
   Can  global  keyword  be  used  without  GV  in  the  program  ?  --->  Yes

2) def  f1():
	   def  f2():
		    nonlocal  x
    Can  nonlocal  keyword  be  used  without  a  local  variable  in  outer()  function  ?  ---> No
'''

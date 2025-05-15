# Find  outputs(Home  work)
def  outer():
	def  inner():
		#nonlocal  x  #  Error :  There  is no  variable  'x'  in outer()  function
		x = 20  #  Creates  Lv  of  inner() function  with  value  20
		print(x)  #   Lv  of  inner() function  i.e.  20
	# End  of  inner  function
	inner()
	#print(x)  #  Error:  There  is  no  Lv  in  outer()  function
# End  of  the  function
outer()
#print(x)  #  Error:  There  is  no  Gv  'x'



'''
1) Can  inner()  function  use  nonlocal  keyword  without  a  Lv  in  outer()  function ?  --->  No

2) Can  outer()  function  use  LV  of  inner()  function ?  --->  No
    Can  inner()  function  use  LV  of  outer()  function ?  --->	Yes  with  nonlocal  keyword
'''

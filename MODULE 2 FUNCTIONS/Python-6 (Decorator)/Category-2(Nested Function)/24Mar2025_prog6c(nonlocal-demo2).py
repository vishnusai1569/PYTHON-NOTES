#  Find  outputs  (Home  work)
def  outer():
	x = 10  # Lv  of  outer()  function
	def  inner():
		#print(x)  #  Error  :  Lv  'x'  does  not  exist
		nonlocal  x  #  Treats  'x'  as   Lv  of  outer()  function
		x = 20   # Lv  of  outer()  function  is  modified  to  20
		print(x)  # Lv  of  outer()  function  i.e.  20
		x += 5  # Lv  of  outer()  function  is  modified  to  25
	# End  of  inner  function
	print(x)   # Lv  of  outer()  function  i.e.  10
	x += 5 # # Lv  of  outer()  function  is  modified  to  15
	inner()
	print(x)  # Lv  of  outer()  function  i.e.  25
# End  of  outer  function
outer()


'''
10
20
25
'''

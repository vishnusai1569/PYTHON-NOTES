#  Find   outputs(Home  work)
def  outer():
	x = 10 #  Lv  of  outer  function
	def  inner():
		global   x  #  Treats  'x'  as  Gv
		x = 20  #  Creates  GV  with  value  20
		print(x) #  Gv  i.e.  20
		x += 5  #  #  Gv  is  modified  to  25
	# End  of  inner  function
	print(x)  #  Lv  of  outer  function  i.e.  10
	x += 5  #  Lv  of  outer  function  is  modified  to  15
	inner()
	print(x)   #  Lv  of  outer  function  i.e.  15
# End  of  outer  function
outer()
print(x) #  Gv  i.e. 25


'''
10
20
15
25
'''

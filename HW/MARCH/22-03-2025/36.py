#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)
		nonlocal  x
		x = 20
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
#error
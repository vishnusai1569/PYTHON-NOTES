# Find  outputs(Home  work)
def  outer():
    x=10
	def  inner():
		nonlocal  x # x not decleared
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)


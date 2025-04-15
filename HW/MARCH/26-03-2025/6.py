#  Find  outputs  (Home  work)
def   decor(fun):
	print(fun . _name_)
	def   inner():
		return   fun() +  2
	return  inner
@decor
def   f1():
	return  10
# End of the function
print('End')
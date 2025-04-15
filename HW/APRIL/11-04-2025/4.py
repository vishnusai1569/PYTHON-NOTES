# Identify  Error (Home  work)
class   c1:
	def  __del__(self,x):
		print('destructor')
a = c1()
a . __del__(25)#c1.__del__() missing 1 required positional argument: 'x'
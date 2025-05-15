# Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('outer  class  c1  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  c2  constructor')
#end of the class
class  c2:
	def __init__(self):
		print('outer  class  c2  constructor')
#end of the class
a = c1()  #    Executes  constructor of  class  c1
b = c1 . c2()    #    Executes  constructor of  inner  class   c2
c = c2()     #    Executes  constructor of  outer  class   c2


'''
outer  class  c1  constructor
inner  class  c2  constructor
outer  class  c2  constructor


Can  outer  class  and  inner  class  have  same  name ?  ---> Yes
'''
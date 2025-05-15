# Identify  Error
class   c1(c2):  #  Error :  parent  class  c2  does  not  exist
	pass
class  c2(c1):  #  Valid : parent  class  c1  exists
	pass
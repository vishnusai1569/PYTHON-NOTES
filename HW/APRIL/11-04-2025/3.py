'''
Find  outputs
Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1()
a = None
b = c1()
del    b
c = c1()
c = c1()
d = c1()
e = c1()

"""
Object  is  created  at  address  :   4378602400
Object  at  address  4378602400  is  lost
Object  is  created  at  address  :   4379872144
Object  at  address  4379872144  is  lost
Object  is  created  at  address  :   4379872144
Object  is  created  at  address  :   4379059488
Object  at  address  4379872144  is  lost
Object  is  created  at  address  :   4379059792
Object  is  created  at  address  :   4378800304
Object  at  address  4379059488  is  lost
Object  at  address  4379059792  is  lost
Object  at  address  4378800304  is  lost
"""
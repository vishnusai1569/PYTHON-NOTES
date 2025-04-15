#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()
print()
del   a
print('Hello')
del   b
print('Hi')
del   c
print('Bye')
d = c1()
print('End')



"""
Object  is  created  at  address  :   4366444800

Hello
Hi
Object  at  address  4366444800  is  lost  
Bye
Object  is  created  at  address  :   4368075344
End
Object  at  address  4368075344  is  lost 
"""
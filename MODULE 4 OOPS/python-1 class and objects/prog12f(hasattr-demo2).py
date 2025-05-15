

# Find  outputs  (Home  work)
class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....')
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....')
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....')
#end of the class
a = [Cat() , Dog() , Goat()] #  List  of  3   objects
for  x  in   a: #  'x'  is  each  object  of  list  'a'
	if   hasattr(x , 'talk'):
		x . talk()
	else:
		x . bark()

'''
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''


'''
Iteration                x             Method  of  which  class  is  executed
-------------------------------------------------------------------------------
     1                       a[0]         Cat  class  method  becoz  'x'  is  Cat  class  object

     2                       a[1]         Dog  class  method  becoz  'x'  is  Dog  class  object

     3                       a[2]        Goat  class  method  becoz  'x'  is  Goat  class  object
------------------------------------------------------------------------------------
'''
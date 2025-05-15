#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()  #  Executes  constructor  only  once  due  to  single   object
del   a # Object  is  not  lost  becoz  there  are  two  more    references  to  the  object
print('Hello')
del   b   # Object  is  not  lost  becoz  there  is  one   more  reference  to  the  object
print('Hi')
del   c #  Executes  destructor before  object  is  lost
print('Bye')
d = c1()  #  Executes  constructor
print('End')
 #  Executes  destructor before  object   'd'  is  lost


'''
Object  is  created  at  address  :  1000
Hello
Hi
Object  at  address  1000  is  lost
Bye
Object  is  created  at  address  :  2000
End
Object  at  address  2000  is  lost
'''


'''
1) When  is  an  object  not  lost  ?  --->  When  there  is  at  least  one  reference  to  the  object

2) When  is  an  object  lost  ?  --->  When  there  are  no  references  to  the  object
'''
# Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		return '__add__ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)  #    __add__()  method  of  class  c1  returns  a  message  i.e.  __add__ method  of  class   c1'
print('a + 7 : ' , a + 7)   #    __add__()  method  of  class  c1  returns  a  message  i.e.  __add__ method  of  class   c1'
#print(7 + a) #  Error  :   __add__()  method  of  int  class  can  not  take  c1  class  object  'a'
print('7 + 8 : ' , 7 + 8)   #    __add__()  method  of  int  class  returns   15
m = c2()
n = c2()
#print(m + n)  #  Error :  No  __add__()  method  in  class  c2
print('a + m : ' , a + m)   #    __add__()  method  of  class  c1  returns  a  message  i.e.  __add__ method  of  class   c1'
#print(m + a)   #  Error :  No  __add__()  method  in  class  c2


'''
Type  of  operand1  plays  a   key  role  in  execution  of  operator  overloading  method
'''
#  Find  outputs (Home  work)
class   c1:
	def  _str_(self):
			return  '25'
class   c2:
	def  _str_(self):
			return   35
class   c3:
	def  _str_(self):
			print('Hyd')
class   c4:
	def  _str_(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a) #  _str_()  method  of  class  c1  returns   '25'
#print(b) #  Error  becoz  _str_()  method  of  class  c2   returns  non-string  i.e.  35
#print(c)  #  Error  becoz  _str_()  method  of  class  c3   returns  non-string  i.e.  None
#print(d) # Error  :   arg  for  _str_()  method  of  class  c4
print(b . _str()) #  __str_()  method  of  class  c2   returns  35
print(c . _str())  #  __str_()  method  of  class  c3   prints  'Hyd'  and  returns  None
print(d . _str(50))    #  __str_()  method  of  class  c4   returns   '50'


'''
25
35
Hyd
None
50
'''


'''
1) Can  _str()  method  return  non-string ?  --->  Yes  when  __str_()  method  is  called  explicitly  and
                                                                                    no  when  _str_()  method  is  automatically  executed

2) Can  _str()  method  have  an  argument ?  --->  Yes  when  __str_()  method  is  called  explicitly  and
                                                                                     no  when  _str_()  method  is  automatically  executed
'''
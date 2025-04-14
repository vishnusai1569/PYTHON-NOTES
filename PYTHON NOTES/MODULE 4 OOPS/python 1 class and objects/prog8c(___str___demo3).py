prog8c(___str___demo3).py

#  Find  outputs (Home  work)
class   c1:
	def  __str__(self):
			return  '25'
class   c2:
	def  __str__(self):
			return   35
class   c3:
	def  __str__(self):
			print('Hyd')
class   c4:
	def  __str__(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a) #  __str__()  method  of  class  c1  returns   '25'
#print(b) #  Error  becoz  __str__()  method  of  class  c2   returns  non-string  i.e.  35
#print(c)  #  Error  becoz  __str__()  method  of  class  c3   returns  non-string  i.e.  None
#print(d) # Error  :   arg  for  __str__()  method  of  class  c4
print(b . __str__()) #  __str__()  method  of  class  c2   returns  35
print(c . __str__())  #  __str__()  method  of  class  c3   prints  'Hyd'  and  returns  None
print(d . __str__(50))    #  __str__()  method  of  class  c4   returns   '50'


'''
25
35
Hyd
None
50
'''


'''
1) Can  __str__()  method  return  non-string ?  --->  Yes  when  __str__()  method  is  called  explicitly  and
                                                                                    no  when  __str__()  method  is  automatically  executed

2) Can  __str__()  method  have  an  argument ?  --->  Yes  when  __str__()  method  is  called  explicitly  and
                                                                                     no  when  __str__()  method  is  automatically  executed
'''
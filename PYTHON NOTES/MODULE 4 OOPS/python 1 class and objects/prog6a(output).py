prog6a(output).py

#  Find  outputs  (Home  work)
class   c1:
	def  m1(self): # self is  object  'a'
		x = 10 #  Local variable of m1() method
		self . x = 20 #  Adds  variable  'x'  to  object  a'  with  value  20
		print(x) #  Local  variable  i.e. 10
		print(self . x) #  Variable  'x'  of   object 'a'   i.e.  20
		x += 5 #  Modifies  local  variable  'x' to  15
		self . x += 7  #  Modifies  variable  'x'  object  'a'  to  15
	def   m2(self):
		#print(x) #  Error :  No  local  variable x in m2()  method
		print(self . x)  #  Variable  'x'  of   object 'a'   i.e.  27
		self . x += 6  #  Modifies  variable  'x'  object  'a'  to  33
# End  of  the  class
a = c1()  #  Creates  empty  c1  cla
a . m1()
a . m2()
print(a . x)  #  33
#print(self . x)  #  Error  becoz  there  is no  self  outside  the  class
#print(x) #error  becoz  there  is  no  global  variable  'x'

'''
10
20
27
33
'''

'''
Local  variable  --->  x = 10
Object  a   --->  x = 20  --->  27   --->  33
'''


'''
1) Who  can  use  self ?  --->  Just   method

2) Who  can  not  use  self ?  ---> Function  and  outside  the  class
'''
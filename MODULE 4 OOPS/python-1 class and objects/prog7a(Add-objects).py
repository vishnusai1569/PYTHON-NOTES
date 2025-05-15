

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 self . x= eval(input('Enter  value  of  x :  '))  #How  to  read  inputs  into  variables  x , y  and  z  of  object  self
		 self . y= eval(input('Enter  value  of  y :  '))
		 self . z= eval(input('Enter  value  of  z :  '))
	def   add(self , m , n):
		 self . x = m . x + n . x #How  to  add  objects  m  and  n  and  store  results  in  object  self
		 self . y = m . y + n . y
		 self .  z = m . z + n . z
	def  disp(self):
		 print('x : ' , self . x)  #  How  to  print  object  self
		 print('y : ' , self . y)
		 print('z : ' , self . z)
# End  of  the  class
a = Test()   #How  to  create  three  Test  class  objects  a , b  and  c
b = Test()
c = Test()
print('First  Object')
a . get()  #How  to  read  inputs  into  object  'a'
print('Second  Object')
b . get()  #How  to  read  inputs  into  object  'b'
c . add(a,b)  #How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c . disp() #How  to  print  object  'c'


'''
object  'a'  --->   x = 10 , y = 20 , z = 30

object  'b'  --->   x == 40 , y = 50 , z = 60

object  'c'  --->   x = 50 , y = 70 , z = 90
'''



'''
1) Is  c = a + b  valid ?   --->  No  becoz  there  is  no  __add__()  method  in  Test  class

2) What  does  print(c)  do ?  --->  Executes  __str__()  method  of  object  class

3) What  does  __str__()  method  of  object  class  do ?  --->  Returns  type  and  address  of  object  'c'
'''


'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  ---> sqrt(s  (s - a)  (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self . a = eval(input('Enter  first  side  of  triangle : '))
		self . b = eval(input('Enter  second  side  of  triangle : '))
		self . c = eval(input('Enter  third  side  of triangle : '))
	def  test(self):
		 if  self . a + self . b > self . c  and  self . b + self . c > self . a  and  self . c + self . a > self . b:
				pass
		 else:
				print('Not  a  triangle')
				exit()
	def  area(self):
			s = (self . a + self . b + self . c) / 2
			return   math . sqrt(s * (s - self . a) * (s - self . b) * (s - self . c))
	def  peri(self):
			return  self . a + self . b + self . c
# End of the class
if   __name__  ==  '__main__':
	t = triangle()  #How  to  create  triangle  class  object
	t . get()  #How  to  read  inputs  into  object
	t . test()  #How  to  test  whether  inputs  are  valid
	print('Area : ',  t . area())
	print('Perimeter : ', t . peri())


#  object  't'  ---> x  =  3  ,  y = 4 ,  z  = 8


'''
1) What  are  a , b , c  called ?  --->  Instance  variables  of  object  't'

2) What  is  's'  called ?  --->  Local  variable  of  area()  method

3) What  is  the  issue  with  t . s = 10 ?  --->  Adds  variable  's'  to  object  't'
																	    but  triangle  class  object  should  have  three  variables  but  not  four

4) How  many  variables  are  in  object  't'  after  execution  of  t = triangle() ?  --->
																										Nothing  becoz  every  object  is  initially  empty

5) How  many  variables  are  in  object  't'  after  execution  of  t . get() ?  --->
											Three  Variables  a , b  and  c  becoz  get()  method  adds  three  variables  to  object  't'
'''



#  Find  outputs
class  c1:
	def __init__(self):
		self.x = 10  #How  to  initialize  public  variable  'x'  with  10
		self.__x = 20 #How  to  initialize  private  variable  'x'  with  20
		self.__x__=30 #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) #How  to  print   variable  'x'
print(a.__x__) #How  to  print  public  dunder  variable  'x'
print(a._c1__x) #How  to  print   private  variable  'x'
#print(a . __x) #  Error  :  Not  visible  outside  the  class
a.m1() #How  to  call  public  method  m1()
a.__m1__() #How  to  call  public  dunder  method  m1()
a . __m1__
a . m1
a._c1__m1() #How  to  call  private  method  m1()
#a . __m1() #error  :  Not  visible  outside  the  class


'''
1) What  is  __x  called ?  --->  private  variable  due  to  double  underscore

2) What  is   x  called ?  --->  Public  variable

3) What  is  __x__  called  ?   ---> public  dunder  variable

4) What  is   __m1  called ?  --->  private  method  due  to  double  underscore

5) What  is  m1  called ?  --->  public  method

6) What  is  __m1__  called ?  --->  public  dunder  method
'''
prog10e(output).py

# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self . x =10 #How  to  initialize  public  variable  'x'  to  10
		self . __y=20 #How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print('variable   x  :  ', self . x) #How  to  print   variable  'x'
		print('private variable y:  ', self . __y) #How  to  print  private  variable  'y'
		self . __m2()#How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print('variable x  :  ', self . x) #How  to  print   variable  'x'
		print('private variable y:  ', self . __y) #How  to  print  private  variable   'y'
# End  of  the  class
t = Test() #   Object is  initialized  with  x = 10  and  __y = 20  by  constructor
print('Outside')
print('variable  x  :  ', t . x) #How  to  print  variable  'x'
print('private variable  ' , t .  _Test__y) #How  to  print   variable  'y'
#print(t . __y) #  Error :  Not   private  variable can  not  be  used  outside the  class  as  it  is  not  visible
print(t . __dict__) # { 'x':10 , '_Test__y':20}
t.m1() #How  to  call  method  m1()
t._Test__m2() #How  to  call   method  m2()
#t . __m2()  #  Error :  private  method  can  not  be  called  outside the  class  as  it  is  not  visible
print('End')


'''
Outside
variable  x  :   10
private variable   20
{'x': 10, '_Test__y': 20}
m1  method
variable   x  :   10
private variable y:   20
__m2  method
variable x  :   10
private variable y:   20
Back to m1 method
__m2  method
variable x  :   10
private variable y:   20
End
'''


'''
1) How  to  access  private  variable  outside  the  class  ?  --->  object . _classname__variablename

2) How  to  access  private  variable  in  the  same  class  ?  --->  object . __variablename

3) How  to  call   private  method  outside  the  class  ?  --->  object . _classname__method()

4) How  to  call   private  method  in  the  same  class  ?  --->  object . __method()
'''
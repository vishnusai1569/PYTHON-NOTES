# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   __init__(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def __init__(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		super() . __init__(a2 , b2)# How  to  call  parent  class  constructor  by  passing  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		super() . disp() # How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40) #  Object  is  initialized  with  a = 10 , b = 20 , c = 30 , d = 40  by   parent  and  child   constructors
y = child()  #  Object  is  initialized  with   default  values  a = 0 , b = 0 , c = 0 , d = 0  by   parent  and  child   constructors
print('Object  x')
x . disp()
print('Object  y')
y . disp()

'''
Object  x
10 <tab> 20 <tab> 30 <tab> 40 <tab>
Object  y
0 <tab> 0 <tab> 0 <tab> 0 <tab>


Object  x  ---> a = 10 , b = 20 , c = 30 , d = 40
Object  y  ---> a = 0 , b = 0 ,  c = 0 , d = 0
'''


'''
1) What  are  the  variables  of  objects  x  and  y ?  --->  a , b , c , d

2) Who  is  initializing  variables  a  and  b ?  ---> Parent  constructor
    Who  is  initializing  variables  c  and  d ?  --->  Child  constructor

3) What  does  object  'x'  contain  when  parent  constructor  is  not  called  from  child  constructor  ? --->
													c =  30  and d  =  40  even  though  10 , 20 , 30 , 40  are  passed  to  the  constructor

4) What  happens  when  there  are  no  default  values  to  parameters  a2 , b2 , c2 , d2 ? --->   y = child()  throws  error
'''
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number    :  '))  #  10
	def  get2(self):
		self . y = int(input('Enter  any  number  :  '))  #  60
		self . z = int(input('Enter  any  number  :  ')) #    70
	def   compute(self):
		Test . x += 1
		self . y  += 1
		self . z  += 1
		self . x  += 1  #  c . x = c . x + 1 --->  c . x = 13 + 1 = 14
	def    disp(self):
		print(Test . x , self . y , self . z ,  self . x , sep = '\t')
# End  of  the  class
Test . get1()
a = Test()  # Three  empty  objects
b = Test()
c = Test()
a . get2()
b . get2()
c . get2()
a . compute()
b . compute()
c . compute()
a . disp()
b . disp()
c . disp()


'''
13      21      31     12
13      41      51     13
13      61      71     14


static   variable   --->   x = 13

Object  'a'  --->  y = 21 , z = 31 , x = 12

Object  'b'  --->  y = 41 , z = 51 , x = 13

Object  'c'  --->  y = 61 , z = 71 , x  = 14
'''
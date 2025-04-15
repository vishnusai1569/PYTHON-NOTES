# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10
		self.__y=20
	def  m1(self):
		print('m1  method')
		print(t.x)
		print(t._Test__y)
		t._Test__m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(t.x)
		print(t._Test__y)
# End  of  the  class
t = Test()
print('Outside')
print(t.x)
print(t._Test__y)
#print(t .__y)
print(t . __dict__)
t.m1()
t._Test__m2()
#t . __m2()
print('End')

'''
Outside
10
20
{'x': 10, '_Test__y': 20}
m1  method
10
20
__m2  method
10
20
Back to m1 method
__m2  method
10
20
End
'''

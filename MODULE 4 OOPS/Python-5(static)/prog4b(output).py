#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)  #  self  is   25
a = c1()
a . m1(35) #  self  is   35

'''
25
35
'''


'''
1) How  many  arguments  can  a  static  method  take ?  --->  0 , 1  (or)  more  than  one

2) Can  static  method  be  called  wrt  object ?  --->  Yes  but  not  recommended
'''
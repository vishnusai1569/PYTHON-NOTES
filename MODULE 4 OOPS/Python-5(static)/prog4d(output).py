#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):  #  Discarded  becoz  another  method  is  defined  with  same  name
		print('static  method')
		print(self)
	def   m1(self): #  Recognized  becoz  it  is  the last  method
		print('instance  method')
		print(self)
#  End  of  the   class
c1 . m1(25) #  Treats   m1  as  static  method  as  m1()  is  called  thru classname
a = c1()
a . m1()  #  Treats   m1  as   instance   method  as  m1()  is  called  thru   object  'a'

'''
instance method
25
instance method
Type  and  address  of  obejct  'a'
'''
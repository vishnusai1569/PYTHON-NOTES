#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)  #   Treats   m1   as  static  method  becoz  it  is  called  thru  classname
a = c1()
a . m1()  #   Treats   m1  as  instance  method  becoz  it  is  called  wrt  object
#a . m1(35) #  Error  due  to  argument  35

'''
25
Type  and  address  of   object  'a'


Is  m1()  a  static  method  (or)  instance  method  ?   --->  static  method  if  it  is  called  thru  classname  and
								                                                            instance  method  if  it  is  called  wrt  object
'''
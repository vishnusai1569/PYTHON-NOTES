# Find  outputs  (Home  work)
class   outer:
	def  __init__(self):
		print('Outer  class  object   is  created')
	def  m1(self):
		print('Outer  class  method')
	class   inner:
		def __init__(self):
			print('Inner  class  object   is  created')
		def m1(self):
			print('Inner  class  method')
#end of the class
o = outer()
o . m1()  #  How  to  call  m1()  method  of  outer  class
i1 = o . inner()
i1 . m1()  #  How  to  call  m1()  method  of  inner  class
i2 = outer . inner()
i2 . m1()  #   How  to  call  m1()  method  of  inner  class  in  another  way
i3 = outer() . inner()
i3 .m1()  #  How  to  call  m1()  method  of  inner  class  in  one  more  way
#i = inner()  #   Error : inner  class  object  can  not  be  created  directly  without  outer  class  object  (or)  outer  class  name

'''
Outer  class  object   is  created
Outer  class  method
Inner  class  object   is  created
Inner  class  method
Inner  class  object   is  created
Inner  class  method
Outer  class  object   is  created
Inner  class  object   is  created
Inner  class  method


1) What  are  the  members  of  outer  class ?  --->  Constructor , m1()  method  and  inner  class

2) What  are  the  members  of  inner  class ?  ---> Constructor  and   m1()  method
'''
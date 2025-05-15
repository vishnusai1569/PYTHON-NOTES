# Find  outputs (Home  work)
from   abc    import    *
class   parent(ABC):
	@abstractmethod
	def  m1(self):
		pass
	@abstractmethod
	def  m2(self):
		pass
	@abstractmethod
	def  m3(self):
		pass
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
class  gc(child):
	def  m2(self):
		print('m2  method  of    gc  class')
class  ggc(gc):
	def  m3(self):
		print('m3  method  of  ggc  class')
# End  of  the  class
a = ggc()
a . m3()  #  Executes  method  of  ggc  class  becoz  'a'  points  to  ggc  class  object
a . m2()   #  Executes  method  of  gc  class  becoz  there  is  no  m2()  in  ggc  class
a . m1()   #  Executes  method  of  child  class  becoz  there  is  no  m1()  in  ggc  and  gc  classes
#parent()  #  Error :  parent  is  an  abstract  class  with  3  abstract  methods   m1() , m2()  and  m3()
#child()  #  Error :   child  is  an  abstract  class  with  2  inherited  abstract  methods  m2()  and  m3()
#gc()   #  Error :   gc  is  an  abstract  class  with  inherited  abstract  method  m3()

'''
m3  method  of  ggc  class
m2  method  of    gc  class
m1  method  of  child  class
'''

'''
1) How  many  abstract  methods  are  in  parent  class ?  ---> Three  abstract  methods  m1() , m2()  and  m3()

2) How  many  abstract  methods  should  child  class  implement ?  ---> All  the  three  methods

3) But  how  many  methods  is  child  class  implementing ?  --->  Only  one  method  m1()

4) Who  should  implement  m2()  and  m3() ? ---> gc  class

5) How  many  methods  is  gc  implementing ?  ---> Only  one  method  m2()

6) Who  should  implement  m3()  method ?  --->  ggc  class

7)     class               concrete  methods               abstract   methods
      -----------------------------------------------------------------------------
	  parent						  0                                          3

	  child							  1                                           2

	  gc								  2                                           1

	  ggc								  3                                           0
'''
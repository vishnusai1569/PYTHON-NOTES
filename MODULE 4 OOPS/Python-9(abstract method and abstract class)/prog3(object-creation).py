# Find  outputs (Home  work)
from  abc  import  *
class  c1(ABC):
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(slef):
		print('c1  class  constructor')
class  c2(ABC):
	def  m1(self):
		pass
	def  __init__(slef):
		print('c2  class  constructor')
class  c3:
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(slef):
		print('c3  class  constructor')
class  c4(c1):
	def  m1(self):
		pass
	def  __init__(slef):
		print('c4  class  constructor')
class  c5(c1):
	def  __init__(slef):
		print('c1  class  constructor')
# End  of  the  class
#c1()   #  Error :  c1 is  an  abstract  class  with  abstract  method  m1()  and  hence  c1  class  object  can  not  be  created
c2()   #  Valid  :   No  abstract  method  in  class  c2  and  hence  c2  class  object  can   be  created
c3()    #  Valid  :   c3  is  not  an  abstract  class   and  hence  c3  class  object  can   be  created
c4()    #  Valid  :   No  abstract  method  in  class  c4  and  hence  c4  class  object  can   be  created
#c5()   #  Error :  c5   is  an  abstract  class  with  inherited  abstract  method  m1()  and  hence  c5  class  object  can  not  be  created


'''
c2  class  constructor
c3  class  constructor
c4  class  constructor
'''
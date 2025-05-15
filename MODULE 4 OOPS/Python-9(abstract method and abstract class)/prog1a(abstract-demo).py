# abstract class  demo  program
from  abc  import  ABC , abstractmethod
class   parent(ABC):
	@abstractmethod
	def   m1(self):
		pass
class  child(parent):
	def  m1(self):
		print('Implementation  method')
#end of the class
#x = parent()  #  Error :  parent  is  an  abstract  class  with  abstract   method  m1()
x = child() #   valid
x . m1() #  Executes  method  of  child  class  becoz  'x'  is  child  class  object


'''
Class                               Does  abstract  method  exist ?    Cab  object  be  created ?
-----------------------------------------------------------------------------------------------------
1) abstract  class							   Yes                                        No

2) abstract  class                           No                                         Yes

3) concrete  class						       Yes                                       Yes

4) concrete  class						       No                                         Yes
'''
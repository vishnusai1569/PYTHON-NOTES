#  Find  outputs (Home  work)
from  prog9a  import  c1  #  Discards  imported  class  c1  becoz  another  class  with  same  name  is  defined  later
class   c1:  #  Recognized
	def  _init_(self):
		print('c1  class  of  prog9b')
a = c1()  #  Executes  constructor of  class  c1  in  same  module  i.e.  c1  class  of  prog9b


'''
Why  is  c1  class  of  prog9a  discarded ?  --->
													Since  another  class  with  same  name  c1  is  defined  in  the  current  module
'''
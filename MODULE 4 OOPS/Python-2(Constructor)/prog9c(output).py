
#  Find  outputs (Home  work)
class   c1:  #  Discarded  becoz  a  class   with  same  name  c1  is  imported  from  prog9a
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1 #  Recognized
a = c1()  #  Executes  constructor  of  class c1  from prog9a  i.e.  c1  class  of  prog9a


'''
1) Why  is  c1  class  of  current  module  discarded ?  --->
																		Since  another  class  with  same  name  c1  is  imported  from  prog9a

2) In  general,  last  class  is  recognized  and  rest  are  discarded
'''
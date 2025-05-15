

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement
from  prog9a   import  c1  as  c2  #  How  to  import  class  c1  from  prog9a   with  from  statement
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a = c1() #  How  to  create  c1  class  object  of  current  module
b = c2()  #   How  to  create  c1  class  object  of  prog9a

'''
c1  class  of  prog9d
c1  class  of  prog9a
'''

'''
We  are  able  to  use  both  the  c1  classes  of  prog9a  and  prog9d  and  this  is  possible  with  member  alias
'''
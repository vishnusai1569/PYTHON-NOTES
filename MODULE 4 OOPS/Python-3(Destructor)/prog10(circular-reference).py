# Costly  Gift
# Circular  reference (Home  work)
class   c1:
	def   __init__(self , k):  #  self  is   object  x . a   and  'k'  is  object  'x'
		print('c1  class  object  is  created')
		self . b = k  #   x . a . b = x   --->  Adds  variable  'b'  to  object  x . a which  points  to  c2 class  object
		print('End  of  c1  class constructor')
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):  #  self  is   object  'x'
		print('c2  class  object  is  created')
		self . a = c1(self)   #   x . a = c1(x)  --->  Adds  variable  'a'  to  object  'x'  which  points  to  c1 class  object
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2()  #  Executes  constructor  of class  c2
print('program end')
#  Executes  destructor  of  classes  c2  and   c1  before  objects  are  lost

'''
Program Begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
Program End
c2  class  object  is  lost
c1  class  object  is  lost
'''



'''
1) c2  class  object  contains  c1  class  object   reference   and  vice-versa.
    This  is  known  as  circular  reference

2) What  are  the  names  of  c2  class  object ?  --->  x   and  x . a . b
     What  is  the  name  of  c1  class  object ?  ---> x . a

3) What  are  the  five  events  after  program  terminates ?  --->
	 a) Global  referece  'x'  is  lost
	 b) c2  class  object  is  lost  as  it  has  no  reference
	 c) c2  class  destructor  is  executed  before  c2  class  object  is  lost
	 d) c1  class  object  is  lost  as  it  has  no  reference
	 e) c1  class  destructor  is  executed  before  c1  class  object  is  lost

4) Is  an  object  lost  when  there  is  an  internal  reference  to  it  in  a   different  object  ?  --->  Yes

5) In  other  words,  object  is  lost  when  there  are  no  external  references  to  it
'''
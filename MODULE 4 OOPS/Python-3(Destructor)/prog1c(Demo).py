'''
Find  outputs
Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1() #   Creates  object  at  address  1000   and  executes  constructor
a = None #   Executes  destructor  before  object  at  address  1000  is  lost
b = c1() #   Creates  object  at  address  2000   and  executes  constructor
del    b   #   Executes  destructor  before  object  at  address  2000  is  lost
c = c1() #   Creates  object  at  address  3000   and  executes  constructor
c = c1()  #   Creates  object  at  address  4000  ,  executes  constructor and  also  executes  destructor  before  object  at  address  3000  is  lost
d = c1() #   Creates  object  at  address  5000   and  executes  constructor
e = c1() #   Creates  object  at  address  6000   and  executes  constructor
#  Executes  destructor   thrice   before  objects  at  addresses  4000 , 5000  and   6000  are   lost

'''
Object  is  created  at  address  : 1000
Object  at  address  1000  is   lost
Object  is  created  at  address  : 2000
Object  at  address  2000  is   lost
Object  is  created  at  address  : 3000
Object  is  created  at  address  : 4000
Object  at  address  3000  is   lost
Object  is  created  at  address  : 5000
Object  is  created  at  address  : 6000
Object  at  address   4000  is   lost
Object  at  address   5000  is   lost
Object  at  address   6000  is   lost
'''


'''
1) What  is  the  order  in  which  objects  are  lost  after  program  terminates  ?  --->
                                                                                                             The   same   order in  which  they  were  created

2) Which  class  destructor  is  executed  when  None  object  is  lost ?  --->
																						NoneType  class  destructor  but  not  c1  class  destrcutor

3) What  does  NoneType  class  destrcutor  do  ?  --->  Nothing  becoz  it  is  an  empty  destructor
'''
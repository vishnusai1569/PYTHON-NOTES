

#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):    #  Discarded  due  to  another  constructor  in  same  class
		print('1st  constructor')
	def  __init__(self):     #  Discarded  due  to  another  constructor  in  same  class
		print('2nd  constructor')
	def  __init__(self):#   Recognzied  as  it  is  the  last  constructor
		print('3rd  constructor')
# End  of  the  class
a = c1()#  Executes  3rd constrctor of class  c1


'''
Which  constructor  is  executed  when  there  are  multiple  constructors  in  the  class ?  ---> The  last  constructor
'''
#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):  # Discarded  due  to  another  destructor  in the  same  class
		print('1st  destructor')
	def  __del__(self):    # Discarded  due  to  another  destructor  in the  same  class
		print('2nd  destructor')
	def  __del__(self): #  Recognized  as  it  is  the  last  destructor
		print('3rd  destructor')
# End  of  the  class
a = c1()
#  Executes  3rd destructor  before   object  'a'  is  lost



'''
1) Which  destructor  is  executed  when  there  are  multiple  destructors  in  the  class  ?  --->  Last  destructor

2) What  about  remaining  destructors ?  --->   Discarded
'''
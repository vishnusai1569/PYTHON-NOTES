

#  Find  outputs  (Home  work)
def   m1():
		print('Function')
class   c1:
	def   m1(self):  #  Discarded  becoz  another  method  is  defined  with  same  name
		print('1st  method')
	def   m1(self):   #  Discarded  becoz  another  method  is  defined  with  same  name
		print('2nd  method')
	def   m1(self): #   Recognzied  becoz  it  is  the  last  method
		print('3rd  method')
# End  of  class  c1
a = c1()
a . m1() # 3rd method
m1() # Function


'''
Which  method  is  executed  when  methods  have  same  name ?  --->  Last   method
'''


#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):  #  Discarded  becoz  another  method is defined  with  same  name
		print('No  argument  method')
	def   m1(self , x):   #  Discarded  becoz  another  method is defined  with  same  name
		print('Single  argument  method : ' , x)
	def   m1(self , x , y): #  Recognized
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) # Two  argument  method : <space> 10  <space> 20
#a . m1(30) #   Error  becoz  arg  is  not  passed  for  'y'
#a . m1()  #   Error  becoz  args   are   not  passed  for   'x'  and  'y'



'''
1) Does  python  support  method  overloading ?  --->  No

2) Does  python  support  function  overloading ?  --->  No

3) Does  python  support  operator  overloading ?  --->  Yes
'''
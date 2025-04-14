# Find  outputs  (Home  work)
def  f1(x):   #  Discarded  becoz  another  function  is  defined  with  same  name
	print('1st  function : ' , x)
def  f1(y):  #  Discarded  becoz  another  function  is  defined  with  same  name
	print('2nd  function : ' , y)
def  f1(z):  #   Recognized  becoz  it  is  the  last   function
	print('3rd  function : ' , z)
f1(z = 10)   #  3rd function : 10
#f1(y = 20)   #  Error  :  Invalid  arg  name  'y'
#f1(x = 30)   #  Error  :  Invalid  arg  name  'x'



'''
Which  function  is  executed  when  multiple  functions  have  got  same  name ?  --->
																		The  last  function  is  executed  and  rest  are  discarded
'''

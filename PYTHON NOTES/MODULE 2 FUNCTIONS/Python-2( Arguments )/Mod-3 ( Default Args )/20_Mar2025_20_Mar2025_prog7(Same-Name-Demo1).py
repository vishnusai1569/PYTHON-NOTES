# Find outputs  (Home  work)
def   add(a , b):  #  Discarded  becoz  another  function  is  defined  with  same name
	print('2-argument  function')
	return a + b
def  add(a , b , c):   #  Discarded  becoz  another  function  is  defined  with  same name
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4): #Recognized
	print('4-argument  function')
	return a + b  + c + d
# End  of  the  function
# last function will be called
print(add(10 , 20 , 30 , 40)) #  'a'  is  10 , 'b'  is   20, 'c'  is  30 , 'd'  is   40
print(add(50 , 60 , 70))  #  'a'  is  50 , 'b'  is   60, 'c'  is  70 , 'd'  is   default  value  4
print(add(80 , 90)) #  'a'  is  80 , 'b'  is   90, 'c'  is   default  value  3  , 'd'  is   default  value  4
print(add(100))  #  'a'  is  100 , 'b'  is   default  value  2 , 'c'  is   default  value  3  , 'd'  is   default  value  4
print(add())  #  'a'  is   default  value  1 , 'b'  is   default  value  2 , 'c'  is   default  value  3  , 'd'  is   default  value  4


'''
4-argument  function
100
4-argument  function
184
4-argument  function
177
4-argument  function
109
4-argument  function
10
'''

'''
Which  function  is  executed  when  multiple  functions  have  got  same  name ?   --->
																										The  function  which  is  defined  last
'''

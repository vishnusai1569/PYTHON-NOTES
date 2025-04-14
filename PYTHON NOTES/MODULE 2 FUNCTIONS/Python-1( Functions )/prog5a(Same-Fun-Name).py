# Find  outputs
def  f1():   # Discarded  becoz  another  function is  defiend  with  same  name
	print('1st  function')
def  f1():     # Discarded  becoz  another  function is  defiend  with  same  name
	print('2nd  function')
def  f1():  #  Recognized becoz  it  is  the  last  function
	print('3rd  function')
f1()  #   3rd  function



'''
1) Can  multiple  functions  have  same  name ?  --->  Yes

2) Which  function  is  executed  when  multiple  functions  have  got  same  name ?  --->  Last  function

3) What  about  remaining  functions  ?  --->  Discarded
'''

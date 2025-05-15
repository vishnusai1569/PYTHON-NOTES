prog8a(class-function-se-name).py

# What  happens  when  function  and  class  have  same  name ?
def   f1():  # Discarded  becoz  a  class  is  defined  with  same  name  later
	print('Function')
	return  25
class   f1:  #   Recognized
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1() #   Executes  constructor  of  class  f1
print(a) #   __str__()  method  of  object  class  returns  type  and  address  of  object  'a'

'''
Constructor
 Type  and  address  of  object  'a'
 '''

'''
1) What  happens  when  function  and  class  have  got  same  name ?  --->
										The  class  (or)  function  which  is  defined  last  is  recognized  and  rest  are   discarded

2) Which  class   __str__()  method  is  executed  for  print(a)  ?  --->
											__str__()  method  of  object  class  becoz  there  is  no  __str__()  method  in  f1  class
'''
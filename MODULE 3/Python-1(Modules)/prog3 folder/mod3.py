# Find  outputs
x = 30
def   disp():
	print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method  of  class  c1  in  same  module')
from  mod1   import  *  #  'x'  is  10  replacing 30
from  mod2   import  *   #  'x'  is  20  replacing  10
print(x)  #  Variable  'x'  of  mod2  i.e.  20
disp()  #  Function  of  mod2   is  executed  (last  function)
a = c1()  #  Creates  mod2 . c1  class  object
a . m1()  #  method  of  mod2 . c1  class  is  executed



'''
1) How  many  variables  are  in  the  above  program ?  --->  Single

2) What  is  the  value  of  'x'  initially ?  --->  30
    What  is  the  value  of   'x'   after  1st  from  statement  is  executed ?  ---> 10  replacing  30
    What  is  the  value  of  x  after  2nd  from  statement   is  executed  ?  --->  20  replacing  10

3) How  many  disp()  functions  are  in  the  program ?  --->  Three

4) Which  function  is  executed  for  disp()  ?  --->   The  last  disp()   function
																				   i.e.  function  of  mod2

5) How  many  c1  classes  are  in  the  program ?  ---> Three  classes

6) a = c1()
    Which  class  object  is  created  ?  --->  The  last  c1  class  object
																	 i.e.  class  of  mod2

*7) Finally,  members  of  last  imported  module  are  used
'''
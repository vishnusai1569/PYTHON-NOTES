# Save  in  cwd \ p1 \ __init__ . py file
print('__init__   module   of   package  ' ,  __name__  ,  ' is  executed')
if  __name__  !=  '__main__':
	import  p1 . mod1 ,   p1 . mod2


'''
1) py  __init__  . py
    What  does  the  above  command  do ?  --->
														Prints  a  msg  and  does  not  import  mod1  and  mod2  as  __name__  is   '__main__'

2) What  does  the  __init__  module  do  when  it  is  executed  automatically ?  --->
												Prints  a  msg  and  imports  mod1  and  mod2  of  package  p1  becoz  __name__  is  'p1'

3) What  is   the  issue  when  'if'  condition  is  omitted ?   --->
																Package  name   p1  throws   error   when  __init__  module  is  executed  directly
																becoz  there  is  no  package  p1  in  p1

4) if   __name__  !=  '__main__':
   	      import  mod1 ,  mod2
    What  is  the  issue  with  the  above  import  statement ?   --->
																py  reuse . py  throws  error  becoz  there  are  no  mod1  and  mod2  in  cwd
'''
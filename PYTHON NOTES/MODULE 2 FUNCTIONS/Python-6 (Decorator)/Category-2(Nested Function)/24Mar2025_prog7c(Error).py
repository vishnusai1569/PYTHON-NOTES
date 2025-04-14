#  Identify  Error
def   f1():
        nonlocal   x  #  Error:  Only  inner  function can  use  nonlocal  keyword



'''
1) What  are  the  two  pre-requisites  to  use  nonlocal  keyword ?  --->
																		a) Only  inner  function  can   use  nonlocal  keyword
																		b) outer()  function  should  have  Lv  with  same  name

2) What  are  the  pre-requisites  to  use  global  keyword ?  --->  Nothing
																		i.e.  Any  function  can  use  global  keyword  even  though  there  is  no  Gv
'''

#  Save  in  any  file   of  cwd
import  p1
p1 . mod1 . f1()  #  How  to  call  function  f1()  of  mod1  in  package  p1
p1 . mod2 . f1()  #  How  to  call  function  f1()  of  mod2  in  package  p1


'''
1) import  p1
    What  are  the  three  events  wrt  the  above  statement ?  --->
	 a) imports  package  p1
	 b) Executes  __init__  module  of  package  p1
	c) Imports  modules  mod1  and  mod2  of  package  p1  due  to  automatic  execution  of  __init__  module

2) What  is  the  advantage  of  __init__  module ?   --->  It  is  used  to  import  all  the  modules  of  same  package
'''
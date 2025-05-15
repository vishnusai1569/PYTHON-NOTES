#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]  #  List  of  2  functions
for  x  in  a:  # 'x'  is  eacg  function  of   list  'a'
	     x()  #  Each  function  is  executed
#a = [def   f3():  print('Hyd') ,  def   f4():  print('Sec')]  #  Error :  Functions  can  not  be  defined  in  the  list
print(a)  # [Type  and  address  of   function   f1 , Type  of  address  of   function  f2]
a = [f1() , f2()] #   Hyd  <next line>  Sec <next  line>
print(a)  #  [None , None]

'''
Hyd
Sec
[Type  and  address  of   function   f1 , Type  of  address  of   function  f2]
Hyd
Sec
[None, None]
'''


'''
1) Which  functions  can  be   defined  in  the  list ?  --->  Lambda  functions  but  not  regular  functions

2) a = [f1() , f2()]
    What  does  the  above  statement  do ?  --->  Executes  functions  f1()  and  f2()
																								and
																			 prints   Hyd  <next  line>  Sec  <next  line>

3) a = [f1() , f2()]
    How  is   the  above  statement  reduced  to  ?  --->  a = [None , None]  becoz  each  function  returns  None  by  default

4) a = [f1 , f2]
    a = [f1() , f2()]
	What  is  the  difference  between  the  above  two  statements ?  --->
											It  is  a  list  of  type  and  address  of  each  function  in  1st  statement  but
											it  is  a  list  of  result  of  each  function  in  2nd  statement
'''

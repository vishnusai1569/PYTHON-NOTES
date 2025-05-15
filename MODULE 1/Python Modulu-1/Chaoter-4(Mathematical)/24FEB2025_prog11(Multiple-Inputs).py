# How  to   read  multiple  inputs  with  input()  function ?
a , b , c   = [eval(x)   for   x   in   input('Enter  any  3   inputs  separated  by   space  :   ') . split()]
print(a , type(a))
print(b , type(b))
print(c , type(c))




'''
1) What  does  input()  function  do  if  input  is  25 <space bar>  10.8  <space bar>  True ? --->  Reads   '25<space>10.8<space> True'

2) What  does  '25 10.8 True' . split()  do ?  --->  Divides  string  into  list  of  strings  based  on  white  space  delimeter
                                                                             i.e. ['25' , '10.8' ,  'True']

3)  Iteration       x           eval(x)  returns                        object
     ---------------------------------------------------------------------------
           1       	      '25'          eval('25')  is  25                          a

	       2             '10.8'       eval('10.8')  is   10.8                     b

	       3		      'True'      eval('True')  is  True                    c

4) [eval(x)   for  x  in   input('Enter  any  3  inputs  separated  by  comma : ') . split(',')]
    What  is  the  advantage  with  the  above  statement ?   --->  Single  statement  reads  multiple  inputs
    What  is  the  dis-advantage  with  the  above  statement ?  --->  Too  much  of  processing  and  difficult  to  understand

5) a , b , c = [eval(x)   for   x   in   input('Enter  any  3   inputs  separated  by  space  :   ') . split()]
    How  to  divide  the  above  statement  into  three  statements  ?  --->	a = eval(input())
														  				                                            b = eval(input())
																		                                            c = eval(input())

6) a = eval(input())
    b = eval(input())
    c = eval(input())
    What  is  the  advantage  of  the  above  three  statements ?   --->	Easy  to  understand
    What  is  the  dis-advantage   of  the  above  three  statements ?  --->	Too  many  statements

7) [eval(x)   for  x  in   input('Enter  any  3  inputs  separated  by  comma : ') . split(',')]
    What  is  the  above  statement  called ?  --->	List  comprehension
'''

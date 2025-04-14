# Which  of  the  following  are  valid  ?  (Home  work)
''''
def   f1(*a , *b): #  Error  due  to  more  than  one  var-arg  parameter
        pass
'''
def  f2(*a , b): # valid  due  to  single  var-arg  parameter
        pass
def  f3(a , *b):  # valid  due  to  single  var-arg  parameter
        pass
def  f4(a , b): # valid  
        pass
def    f5(a , *b , c):   # valid  due  to  single  var-arg  parameter
        pass
'''
def   f6( * , a , *b , c): #  Error  becoz   a  and  b  can   not  be  ka's
       pass
def   f7(a , *b , c ,  /): #  Error  becoz    c  can   not  be   pa
       pass
'''


'''
1) How  many  var-arg  parameters  can  be  in  a  function ?  ---> At  most  one  

2) def   f6(* , a , *b , c):
		pass
   What  does  first  *  indicate ?  --->   a , b , c  should  be  KA's  only
   Can  argument  'b'  be  a  keyword  argument ?  --->  No  becoz  Var-arg   parameter  should  be  PA
   Can  argument  'a'  be  a  keyword  argument ?  --->  No  becoz  it  is  before  var-arg  parameter

3) def   f7(a , *b , c ,  /):
           pass
    What  does  /  indicate ?  --->  a , b  and  c  should  be  PA's  only
    Can  argument  'c'  be  a  positional  argument ?  --->  No  becoz  argument  after  var-arg  parameter  should  be  a  KA
'''

#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a : 10 <tab> b : (20 , 30 , 40) <tab> c : 50
f1(60 , 70 , c = 80) # a : 60 <tab> b : (70,) <tab> c : 80
f1(90 , c = 100) # a : 90 <tab> b : () <tab> c : 100
#f1(a = 1 , 2 , c = 3) # error  due  to  pa   after  ka
#f1(1 , 2 , 3) #  a  is  1 , b  is  (2 , 3)  and  throws  error  as  arg  is  not  passed  for  'c'
#f1(a = 1 , b = 2 , c = 3) # error  becoz  'b'  can  not  be  ka  as  it  is   var arg parameter
#f1(a = 25 , 100 , 200 , 300 , c = 35)   # error  due  to  pa   100  after  ka   a = 25



'''
def   f1(a , *b , c):
        	pass

1) Can  'b'  be  a  keyword   argument ?  --->  No  becoz  it  is  a  var-arg  parameter

2) Can  'c'  be  a  positional  argument ?  --->  No  becoz  it  is  after  var-arg  parameter

3) Can  'a'  be  a  keyword  argument ?  --->  No  becoz  'b'  is  PA  i.e.  There  can  not  be  KA  before  PA

4) Is  f1(KA , PA , KA)  valid ?  --->  No  becoz  Positional  argument  can  not  be  after  keyword  argument

5) f1(10 , 20 , 30 ,  40)
    What  is  the  issue  with  the  above  function  call ?  ---> No  becoz  'a'  is  10 , b  is  (20 , 30 , 40)  and
															                                argument  is  not  passed  for  parameter  'c'

6) Finally,  what  is  the  order  of  arguments  to  call  f1()  function  ?  --->   f1(PA , Any  number  of  PA's , KA)
'''

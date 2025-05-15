#  Save  in  any  file  of  cwd
from p1.mod1 import *  # How  to  import  members  of  mod1  in  package  p1  with  from  statement
print(x) # How  to  print  variable  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = c1()
a . m1()  # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.mod2 import *  # How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x) # How  to  print  variable  'x'  of   mod2  in  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  package  p1
a = c1()
a . m1()  # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x) #  Error :  package  p1 is not imported
#print(mod1 . x) #  Error  :  mod1 is not imported
#from  p1   import  mod1 . *   #  Error  :  '.'  can  not  be  used   in import clause


'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1
'''


'''
1) from   p1  import  mod1
    from   p1  import  mod2
    How  to  combine  the  above  two  statements  to  a  single  statement ?  ---> from  p1  import  mod1 , mod2

2) from  p1 . mod1 , p1 . mod2  import  *
    Is  the  above  statement  valid ?  ---> No  becoz  members  can  be  imported  from  only  one  module  at  a  time  but  not
															     from  multiple  modules

3) import  p1 . mod1 , p1 . mod2
    Is  the  above  statement  valid ?  --->  Yes  becoz  multiple  modules  can  be  imported  at  a  time

4) import  p1 . mod1 , mod2
    What  does  the  above  statement  do ?  --->  Imports  mod1  from  package  p1  and  mod2  from  cwd
'''
'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
from p1.mod1 import *  # How  to  import   members  of  mod1   in  package  p1  with  from  statement
from p1.mod2  import x as x2 , f1 as f12 , c1 as c12 # How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x) # How  to  print  variable  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = c1()
a . m1()  #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(x2) # How  to  print  variable  'x'  of   mod2  in  package  p1
f12() # How  to  call  function  f1()  of   mod2  in  package  p1
a = c12()
a . m1()  # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1

'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1
'''

'''
How  to  use  members  of  both  the  modules  without  importing  modules ?  --->  With  member  alias
'''
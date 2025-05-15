# Save  in  any  file  of  cwd
from  p1   import  mod1    #   Executes  __init__  module  of  package  p1
print(mod1.x) # How  to  print  variable  'x'  of  mod1  in  package  p1
mod1.f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = mod1.c1()
a.m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
#print(p1 . x) # error as  package  p1  is not imported
#print(p1 . __init__ . x) #  Error  becoz   package  p1   is  not  imported
#print(__init__ . x) #  Error  becoz  there  is  no   __init__  module  in  cwd



'''
__init__   module  of  package  p1  is  executed
20
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
'''



'''
from  p1  import  mod1
Can  members  of  mod1  be  used ?  ---> Yes  with  mod1 . member
Can  members  of  __init__  module  be  used ?  --->  No  becoz  __init__  module  is  not  imported  from   package  p1
'''
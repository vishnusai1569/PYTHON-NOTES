# Save  in  any  file  of  cwd
import  p1 . mod1   #   Automatically  executed  p1 . __int__  module
print(p1 . mod1 . x)  # How  to  print  variable  'x'  of  mod1  in  package  p1
p1 . mod1 . f1()  # How  to  call  function  f1()  of  mod1  in  package  p1
a = p1 . mod1 . c1()
a . m1()  #  How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
#print(p1 . x)  #  How  to  print  variable  'x'  of  __init__  module  in  package  p1
#p1 . f1()  #  How  to  call  function  f1()  of  __init__  module  in  package  p1
a = p1 . c1()
a . m1()  #  How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1
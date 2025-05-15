# Save  in  any  file  of  cwd
import p1 . __init__  # How  to  import  __init__  module  of  package  p1  with  import  statement
print(p1.x) # How  to  print  variable  'x'  of   __init__  module   in   package  p1
p1.f1() # How  to  call  function  f1()  of   init  module  in  package  p1
a = p1.c1()
a . m1()  # How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
print(p1.__init__.x) # How  to  print  variable  'x'  of   __init__  module   in   package  p1  in  another  way
p1.__init__.f1() # How  to  call  function  f1()  of   __init__  module  in  package  p1  in  another  way
a = p1.__init__.c1()
a . m1()  #How  to  call  method  m1()  of  class  c1  in   __init__  module  of  package  p1  in  another  way
#print(p1 . mod1 . x) # error as mod1 is not imported

'''
__init__   module  of  package  p1  is  executed
__init__   module  of  package  p1.__init__  is  executed
10
package  p1 ---> __init__  module ---> f1  function
package  p1 ---> __init__  module ---> class  c1  ---> m1  method
10
package  p1 ---> __init__  module ---> f1  function
package  p1 ---> __init__  module ---> class  c1  ---> m1  method
'''
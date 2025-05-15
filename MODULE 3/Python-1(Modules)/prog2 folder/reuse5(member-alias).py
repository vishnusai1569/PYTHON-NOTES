# Member  alias
from cal import x as o , mul as m , add as d ,  c1 as e1  #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(o) # How  to  print  variable  'x'  of  cal   module
#print(x) # Error  :  There  is  no  object  'x'  in  current  module
print(d(10 , 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(m(10 , 7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
n = e1()
n . m1()  #How  to  call  m1()  method  of  class  c1  in  cal  module
#print(add(10 , 7))  # Error  :  There  is  no   add()  function  in  current  module
#b = c1()   # Error  :  There  is  no  class  c1   in  current  module



'''
100
17
70
m1  method
'''

# cal . py , reuse1 . py , reuse2 . py ,  reuse3 . py , reuse4 . py ,  reuse5 . py  should  be  in  same  folder  (prog2  folder)
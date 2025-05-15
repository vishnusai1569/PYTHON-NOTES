# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from  cal  import  *  #  How  to  import  all  the  members  of  cal  module  with  from  statement
print(x)  #  How  to  print  variable  'x'  of  cal   module   --->   100
print(y)  #  How  to  print  variable  'y'  of  cal   module   --->  200
#print(cal . x)   # Error :  cal  module  is  not  imported
print(add(10 , 7))  #  How  to  call  add()  function  of  cal  module  by  passing  10  and  7   --->  17
print(sub(10 , 7))  #  How  to  call  sub()  function  of  cal  module  by  passing  10  and  7   --->  3
print(mul(10 , 7))  #  How  to  call  mul()  function  of  cal  module  by  passing  10  and  7   --->  70
print(div(10 , 7))  #  How  to  call  div()  function  of  cal  module  by  passing  10  and  7  --->  1.42
#print(cal . add(x , y))  # Error :  cal  module  is  not  imported
a = c1()
a . m1()  # How  to  call  m1()  method  of  class  c1  in  cal  module  --->  m1  method
#b = cal . c1()  # Error :  cal  module  is  not  imported
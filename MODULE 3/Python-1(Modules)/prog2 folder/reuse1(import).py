
# How  to  use  members  of  cal  module  with  import  statement ?  (Home  work)
print('Begin')
import  cal  #  How  to  import  cal  moudle  with  import  statement
print(cal . x)  #  How  to  print  variable  'x'  of  cal   module  ---> 100
print(cal . y) #  How  to  print  variable  'y'  of  cal   module  --->  200
#print(x)   #  Error :  No  'x'  in   current  module
print(cal . add(10 , 7))  #  How  to  call  add()  function  of  cal  module  by  passing  10  and  7  --->  17
print(cal . sub(10 , 7))  #  How  to  call  sub()  function  of  cal  module  by  passing  10  and  7   --->   3
print(cal . mul(10 , 70))   # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7  --->  70
print(cal . div(10 , 7))  #  How  to  call  div()  function  of  cal  module  by  passing  10  and  7   --->  1.42
#print(add(cal . x , cal . y))  #   Error :No  add()  function  in  current  module
a = cal . c1()  # Creates  c1  class  object
a . m1() #   How  to  call  m1()  method  of  c1  class  in  cal  module  --->  m1  method
#b = c1()  #  Error :  No  class  c1  in  current  module
#cal . c1 . m1()   #Error :  method  can  not  be  called  thru  classname
#m1()  #  Error :  No  function  m1()  in  current  module



'''
1) What  is  the  syntax  to  create  an  object ?  --->  object =  classname()

2) How  to  call  method  of  a  class ?  --->  object . method()

3) Is  classname . method()  valid ?  --->  No  becoz  method  should  be  called  wrt  object  but  not  thru  classname

4) Is  method()  valid ?  --->  No  becoz  method  can  not  be  called  directly  without  object
'''
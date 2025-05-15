

# Module  alias
print('Begin') # Begin
import cal as c   #How  to  import  cal  module  with   another  name  using  import  statement
print(c . x) # How  to  print  variable  'x'  of  cal   module
print(c . y) # How  to  print  variable  'y'  of  cal   module
print(c . add(10 , 7)) # How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(c . sub(10 , 7)) # How  to  call  sub()  function  of  cal  module  by  passing  10  and  7
print(c . mul(10 , 7)) # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print(c . div(10 , 7)) # How  to  call  div()  function  of  cal  module  by  passing  10  and  7
d = c . c1()
d . m1()  # How  to  call  m1()  method  of  c1  class  in  cal  module
#print(cal . x) # error becoz cal module is not imported
#from  math  as   m  import  * # error becoz module alias is not allowed in from statement

'''
Begin
100
200
17
3
70
1.4285714285714286
m1  method
'''


'''
1) Why  is  module  alias  not  permitted  in  from  statement ?  --->  Since  members  are  imported  but  not  module

2) How  to  perform  module  alias ?  --->  With  import  statement  and  as  keyword

3) How  to  perform  member  alias ?  --->  With  from  statement  and  as  keyword
'''
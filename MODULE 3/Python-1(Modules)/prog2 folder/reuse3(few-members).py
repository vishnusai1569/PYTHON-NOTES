

# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin') # Begin
from cal import x , add , mul , c1   #  How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle  with  from  statement
print(x) #How  to  print  variable  'x'  of  cal   module
#print(y) #  Error  :   There  is  no  object  'y'  in  current  module
#print(cal . x) #  Error:  cal module is not imported
print(add(10 , 7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7
#print(sub(10 , 7)) #  Error  :   There  is  no  function   sub()   in  current  module
print(mul(10 , 7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
#print(div(10 , 7))  #  Error  :   There  is  no  function   div()   in  current  module
d = c1()
d . m1()  #    How  to  call  m1()  method  of  class  c1  in  cal  module

'''
Begin
100
17
70
m1  method
'''
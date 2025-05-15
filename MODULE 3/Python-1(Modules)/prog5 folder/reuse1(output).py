#  Find  outputs
from  cal  import  *    #  Imports  those  members  of  cal  module  which  are  in  __all__  list  i.e. add , x , mul  and  c1
print(x)  #  100
print(y)  #   Error :  'y'  is  not  imported
print(add(10 , 7))  #  17
print(sub(10 , 7))   #   Error :  sub()  is  not  imported
print(mul(10 , 7))  #  70
print(div(10 , 7))  #   Error :  div()  is  not  imported
a = c1()  #  Creates  c1  class object
a . m1()  #  Executes  method  of  class  c1
#  abs()  function  demo  program
from  builtins  import  abs  #   Optional  becoz  abs  is  automaticallyy imported
print(abs(-35.8))  #   35.8
print(abs(-27))  #  27
print(abs(29.5))  #   29.5
print(abs(32))  #  32
import  builtins  #  Mandatory  becoz  builtins  module  is  not  imported  automcatically
print(builtins . abs(-25))  #  25


'''
1) What  is  the  simiarity  between  abs()  and  fabs()  ?  --->  Both  the  functions  convert  -ve   value  to  +ve  value

2) What  is  the  result  of  abs(integer) ? ---> Positive  integer
    What  is  the  result  of  abs(float) ?  ---> Positive  float
    What  is  the  result  of  fabs(integer  (or)  float) ?  ---> Always  float

3) Can  abs()  function  be  called  without  import ?  --->  Yes  becoz  it  is  a  function  of  builtins  module
														                                  and  hence  automatically  imported
    Can  fabs()  function  be  called  without  import ?  --->
														No  becoz  it  is  not  automatically  imported  as  it  is  a  function  of  math  module
'''

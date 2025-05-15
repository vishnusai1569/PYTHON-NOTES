#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  Previous  integer  of  10.8  i.e.  10
print(math . ceil(10.8))  #  Next  integer  of  10.8  i.e.  11
print(math . floor(25.0))  #   25  due  to  .0
print(math . ceil(25.0))   #   25  due  to  .0
print(math . floor(-3.5)) #  -4  due  to  -ve  number
print(math . ceil(-3.5))   #  -3
print(math . floor(-9.0))  # -9  due  to  .0
print(math . ceil(-9.0))   # -9  due  to  .0
print(math . floor(25.1)) #   25
print(math . ceil(25.1))   #  26
#print(floor(3.5))     #  Error  becoz  there  is  no  floor()  function  in  current  module
#print(ceil(3.5))    #  Error  becoz  there  is  no  ceil()  function  in  current  module



'''
1) What  does  floor(x)  do ?  --->  Returns  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  next  integer  of  'x'
'''

#  pi  variable ,   degrees()  and  radians()   functions  demo  program
import  math
print(math . pi)  #  22 / 7 = 3.14159
print(math . degrees(math . pi))  #  Converts  pi   radians  to  180  degrees
print(math . degrees(math . pi / 2))  #  Converts  pi / 2   radians  to  90  degrees
print(math . radians(180))  #  Converts  180  degrees  to  pi  radians  = 3.14159
print(math . radians(90))  #  Converts  90  degrees  to  pi / 2  radians  =  1.57
#print(pi)  #  Error  becoz  there  is  no  object  pi  in  current  module



'''
1) What  does  degrees(x)  do ?  --->  Converts   'x'  radians  to  degrees

2) What  does  radians(x)  do ?  --->  Converts  'x'  degrees  to  radians

3) print(math . pi)
    Where  is  pi  searched ?  --->  In  math  module  due  to  the  prefix  math

4) print(pi)
    Where  is  pi  searched ?  --->  In  current  module  becoz  there  is  no  prefix  math

5) math . pi()
    Is  the  above  statement  valid ?  --->  No  becoz  pi  is  an  object  but  not  a  function
'''

#  bool()  function  demo  program
print(bool(0)) #   Converts  0  to  False
print(bool(10))  #   True  becoz  10  is  non-zero  number
print(bool(-25))   #   True  becoz   -25  is  non-zero  number
print(bool(0.0))  #  False  due  to   0.0
print(bool(0.1))   #   True  becoz  0.1  is  non-zero  number
print(bool(0 + 0j))   #  False  becoz  both  real  and  imag  are  zeroes
print(bool(10 + 20j))   #   True  becoz   10 is  non-zero
print(bool(-15j))    #   True  becoz   -15   is  non-zero
print(bool('False'))   #  True  becoz  'False'  is  non-empty  string
print(bool(''))   #   False   due  to  empty  string
print(bool('Hyd'))   #  True  becoz  'Hyd'  is  non-empty  string
print(bool(' '))   #  True  becoz  ' '  is  non-empty  string
print(bool('True'))   #  True  becoz  'True'  is  non-empty  string



'''
bool()  function
------------------
1) What  does  bool(x)  do  ?  --->  Converts  object  'x'  to  True / False

2) Is  0  True  (or)  False ?   ---> False
    What  about  non-zero ?   ---> True

3) Is  ''(i.e.  Empty  string)  True  (or) False ?  --->  False
    What  about  non-empty  string ?  --->  True

4) When  is  x + yj  treated  as  False ?  ---> When  both  'x'  and  'y'  are  zeroes
     When  is  x + yj  treated  as True ?  --->  When  either  'x'  is   non-zero  (or)  'y'  is  non-zero
'''

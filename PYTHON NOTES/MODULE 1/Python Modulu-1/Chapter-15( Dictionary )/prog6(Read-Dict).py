#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a) # '{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}'
print(type(a)) # <class 'str'>
b = eval(a)   #  Converts  string  dict  to  dict
print(b) # {10: 'A', 20: 'D', 15: 'C'}
print(type(b)) # <class 'dict'>



'''
1) Let  input  be  dict(),
    What  does  input()  function  read ?  --->  'dict()'
    What  does  eval('dict()')  do ?  --->  Converts  'dict()'  to  { }

2) Let  input  be  { },
    What  does  input()  function  read ?  --->  '{ }'
    What  does  eval('{ }')  do ?  --->  Converts  '{}'  to  { }

3) Let  input  be  {10 : 20 , 10 : 30}
    What  does  input()  function  read ?  --->  '{10 : 20 , 10 : 30}'
    What  does  eval('{10 : 20 , 10 : 30}')  do ?  --->  Converts   '{10 : 20 , 10 : 30}'  to  {10 : 30}
'''

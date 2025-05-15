# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)  #  Converts  tuple  to  list
print(b)#   [10,20,15,18]
print(type(b))  #  <class  'list'>
print(a  is  b)  # False  becoz  they  point to  different  objects
print(a == b)  # False  becoz  they  point to  different  objects


'''
1) What  does  list ==  tuple  do ?  --->   Compares  references  but  not  objects  even  though  ==  is  used
										                       becoz  they  are  different  class  objects

2) What  is  the  result  of  list  ==  tuple ?  --->  Always  False  becoz  references  point  to  different  objects

3) obj1 == obj2
     When  are  objects  compared  ?  --->  When  both  of  them  are  same  class  objects

4) 10 == 10.0
    What  are  compared (objects / references) ?  --->  Objects  becoz  they  are  non-sequences
'''

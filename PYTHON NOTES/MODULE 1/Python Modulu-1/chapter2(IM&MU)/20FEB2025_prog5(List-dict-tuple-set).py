 #Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]  #  Ref  'a'  points  to  list
b = [10 , 20 , 15 , 18]   #  Ref  'b'  points  to    another  list  becoz  list  is  mutable  and  not  reusable
print(a  is  b)  #  False  becoz  'a' and  'b'  point  to  different  lists
c =  {10 : 20, 30 : 40}  #  Ref  'c'  points  to  dictionary
d =  {10 : 20, 30 : 40}  #  Ref  'd'  points  to    another  dictionary  becoz  dict  is  mutable  and  not  reusable
print(c  is  d)  #  False  becoz  'c' and  'd'  point  to  different  dictionaries
e = (10 , 20 , 15 , 18)  #  Ref  'e'  points  to   tuple
f = (10 , 20 , 15 , 18)#  Ref  'f'  points  to   same  tuple  becoz   tuple  is   immutable  and   reusable
print(e  is  f)   #  True  becoz  'e' and  'f'  point  to  same  tuple
g = {10 , 20 , 15 , 18}  #  Ref  'g'  points  to  set
h = {10 , 20 , 15 , 18}  #  Ref  'h'  points  to    another  set  becoz  set  is  mutable  and  not  reusable
print(g  is  h)  #  False  becoz  'g' and  'h'  point  to  different  sets

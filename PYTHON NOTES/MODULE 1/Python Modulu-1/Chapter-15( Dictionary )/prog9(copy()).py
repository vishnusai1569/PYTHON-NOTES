# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18} can be any order
b = a . copy()  #  Copies  elements  of  set   'a'  to  'b'
print(b) # {10 , 20 , 15 , 18} can be any order
print(a  is  b) # False  becoz  a and b points to different sets
print(a  ==  b) # True  becoz  sets  a and b have same elements
c = a #   Ref  'c'  points  to  set   'a'
print(a  is  c) # True as a and c points to the same set



'''
1) What  does  copy()  method  do ?  --->  Copies  elements  of  a  set  to  another  set   i.e. Object  copy

2) a = b
    What  does  the  above  statement  do  when  'b'  is   a  set ?  --->  Reference  copy
																												i.e.  id  is  copied

3) What  is  shallow  clone ?  ---> Reference  copy
     What  is  deep  clone ?  ---> Object  copy
'''

# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)  # {10,20,15,18}  in  any  order
b = a . copy()  # Copies  elements  of  set  'a' to  'b'
print(b)  # {10,20,15,18}  in  any  order
print(a  is  b)#  False  becoz  'a'  and 'b'  point  to  different  sets
print(a  ==  b)  #  True  due to  same  elements  in  sets  'a'  and  'b'
c = a  #  'c'  points  to  set  'a'
print(a  is  c)  # True  becoz  'a'  and  'c'  point  to  same  set



'''
1) What  does  copy()  method  do ?  --->  Copies  elements  of  a  set  to  another  set   i.e. Object  copy

2) a = b
    What  does  the  above  statement  do  when  'b'  is   a  set ?  --->   Reference  copy
																										       i.e.  id  is  copied

3) What  is  shallow  clone ?  ---> Reference  copy
     What  is  deep  clone ?  ---> Object  copy
'''

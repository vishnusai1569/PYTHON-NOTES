#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a  #   Ref  'b'  points  to  list  'a'
print(a  is  b)  #  True
print(a  ==  b)   #  True
b[2] = 12  #  Modifying   list  'b'  is  as  good  as  modifying  list  'a'
print(a)  #  [10,20,12,18]


'''
1) What  is  shallow  clone ?  --->  Reference  copy  but  not  object  copy

2) What  does  b = a   do  ? --->  Assigns  reference  'b'  to  list  'a'

3) Is  b = a  shallow  clone ?  --->  Yes

4) In  other  words,  b = a  does  not  copy  elements  of  list  'a'  to  list  'b'

5) How  many  lists  are  in  the  above  program ?  --->  Single  list  with  two  references   a  and  b

6) b[2] = 12
    Modifying  list  'b'  is  as   good  as  modifying  list  'a'  becoz  'a'  and  'b'  point  to  same  list
'''

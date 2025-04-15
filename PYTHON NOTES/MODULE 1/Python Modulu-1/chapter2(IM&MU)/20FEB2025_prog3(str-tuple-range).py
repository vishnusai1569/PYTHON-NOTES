#  Find  outputs (Home  work)
a = 'Hyd'   # Ref  'a'  points  to  'Hyd'
print(id(a))  #  Address  of  object 'Hyd'  (may  be  1000)
#a[1] = 'e'  #  Error  becoz  str  object  is   immutable
a = 'Sec'  #Ref  'a'  is  modified  to  another  object  'Sec'
print(id(a))   #  Address  of  object 'Sec'  (may  be  2000)
b = (10 , 20 , 15 , 18)  # Ref  'b'  points  to   tuple
print(id(b))  #  Address  of  tuple  (may  be  3000)
#b[2] = 19  # Error  becoz  tuple  is  immutable
b = (30 , 40 , 35 , 32)   #Ref  'b'  is  modified  to  another  tuple
print(id(b))   #  Address  of  2nd  tuple  (may  be  4000)
c = range(5)  # Ref  'c'  points  to   range  object
print(id(c))  #  Address   of   range  object  (may be  5000)
#c[3] = 10   # Error  becoz  range  object   is  immutable
c = range(5)   #Ref  'c'  is  modified  to  another  range  object  becoz   it  is  not  reusable
print(id(c))   #  Address   of   2nd  range  object  (may be  6000)



'''
1) a = 'Hyd'
    a = 'Sec'
    What  is  modified  when   a = 'Sec'  is  executed  ?  --->  Reference  but  not  object

2) b = (10 , 20 , 15 , 18)
    b = (30 , 40 , 35 , 32)
    What  is  modified  when  b = (30 , 40 , 35 , 32)  is  executed  ?  --->  Reference  but  not  object

3) c = range(5)
    c = range(5)
    What  is  modified  when  c = range(5)  is  executed  ?  --->  Reference  but  not  object
'''

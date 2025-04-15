#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)  #  'a'  is  tuple  due  to  ()
print(a)  #  (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a)  #  Unpacks  tuple  into  elements  i.e.  25  <space> 10.8  <space>  Hyd  <space> True  <space> 3+4j  <space>  None  <space> Hyd  <space> 25
print(type(a))  # <class  'tuple'>
print(len(a))  #  8
print(a[2 : 5])  # Tuple  from  indexex  2  to  4  in  steps   of  1  i.e.  ('Hyd' , True , 3+4j)
print(*a[2 : 5])  #  Unpacks  sub-tuple  --->  Hyd  <space> True  <space> 3+4j
#a[2] = 'Sec'  #  Error  becoz  tuple  is immutable
#a . append('Sec')  # Error  becoz  there  is  no  append()  method in  tuple
#a . remove('Hyd')  # Error  becoz  there  is  no  remove()  method in  tuple
b =  10 , 20 , 30 #  Valid  becoz  ()  are  optional
print(b)  #  (10 , 20 , 30)
print(b * 2)  #  Repeats  tuple  twice  i.e.  (10 , 20 , 30 , 10 , 20 , 30)
c = 40 , 50 , 60,  # Valid  and  last  comma  is  optional
print(c) #  (40 , 50 , 60)
print(type(c))#  <class  'tuple'>

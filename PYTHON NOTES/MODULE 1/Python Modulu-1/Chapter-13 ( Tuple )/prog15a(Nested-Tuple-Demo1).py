#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)  #  ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))  #  <class  'tuple'>
print(len(a))#  3
print(a[0])  #  How  to  print  1st  inner  tuple  i.e. (10,20)
print(a[1])  #  How  to  print  2nd  inner  tuple  i.e.  (30,40,50)
print(a[2])  #  How  to  print  3rd  inner  tuple  i.e.  (60,70,80,90)
print(a[0][1])  #  How  to  print  20
print(a[1][2])  #  How  to  print  50
print(a[2][3])  #  How  to  print  90



'''
1) What  is  a  nested  tuple ?  ---> A  tuple  inside  another  tuple

2) Is  ((10 , 20 , 30))  a  nested  tuple ?  ---> No  becoz  comma  is   missing  and  it  is  treated  as
																	  a  single  tuple  of  three  elements

3) Is  (())  a  nested  tuple ?  ---> No  becoz  comma  is   missing  and  it  is  treated  as  empty  tuple
'''

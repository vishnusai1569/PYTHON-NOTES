# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) #  True becoz  lists  'a'  and  'b'  have  same  elements
print(a  is   b)#   False  becoz  'a'  and  'b'  point  to  different  lists
print(a < c)   #  True  becoz  15 < 25
print(a > d)  #  True  becoz  15 >  7
print(a >= c)  #  False  becoz  15 is  not  >=  25
print(a <= d)   #  False  becoz  15 is  not  <=  7
print(a != c)  #  True  becoz  15  !=  25
print(a != b) #  False  due to  same  elements
print(a == c)   #  False  becoz  15 is  not  =  25


'''
1) Can  lists  be  compared  with  > , < , ==  and  so  on ?  --->  Yes  only  in  python

2) What  are  compared  when  == , >  , < , >= , <=  and  !=  are  used  between  lists ?  --->  1st  non-matching  elements

3) What  does  list1 == list2  do ?  --->  Compares  objects   i.e.  lists
    What  does  list1  is  list2  do  ?  --->  Compares  references  i.e.  id's

4) Can  there  be  multiple  lists  with  same  elements ?  --->  Yes  becoz  list  is  mutable  and  not  reusable
'''

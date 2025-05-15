#  Find  outputs  (Home  work)
a = range(10 , 20)  #   range(10 , 20 , 1)  --->  Object  contains  elements  from  10  to  19  in steps  of  1 
print(*a , sep = ',')  #  10,11,12,13,....19
b = range(5)  #   range(0 , 5 , 1)  --->  Object  contains  elements  from  0  to   4  in steps  of  1 
print(*b)  #   0  <space>  1  <space>  2  <space>  3  <space>  4
c = range(10 , 1 , -1)   #   Object  contains  elements  from   10   to   2  in steps  of  -1 
print(*c , sep = '...') #   10  ... 9 ... 8 ...   ....  2
d = range(-10 , 0)   #   range(-10 , 0 , 1)  --->  Object  contains  elements  from  -10  to   -1   in steps  of  1 
print(*d)   #  -10  <space>  -9  <space>  -8 ...  -1
e = range(-10)   #   range(0  ,  -10 , 1)  --->  Empty   object  becoz  0 >=  -10
print(*e)  #  Unpacks  empty  object  i.e.  Nothing
f = range(2 , 2)  # range(2 , 2 , 1)   --->  Empty   object  becoz  2  >=  
print(*f)  #  Unpacks  empty  object  i.e.  Nothing
#g = range(10 , 11 , 0.1)  # Error  becoz  range  object  can  not  hold  float  elements
#h = range('A' , 'F')   # Error  becoz  range  object  can  not  hold  str   elements


'''
1) range(x , y , +ve  step)
    When  is  range  object  empty ?  ---> When  x >=  y

2) range(x , y , -ve  step)
    When  is  range  object  empty ?  ---> When  x <=  y
'''

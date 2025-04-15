# Find  outputs    (Home  work)
a = range(10 , 50 , 5) #   Object  contains  elements  from  10  to  49  in steps  of  5
print(type(a))   #  <class  'range'>
print(a)  #   range(10 , 50 , 5)
print(*a)  #  Unpacks  object 'a'  to  elements  i.e.  10  <space>  15  <space>  20 <space>  25  <space>  30  <space>  35  <space>  40  <space>  45
print(id(a))  # Address  of  range  object
print(len(a))  #   8
print(*a[2 : 7] , sep = ' , ')  # *a[2 : 7 : 1]  --->  Elements  of  object  'a'  from  indexes  2  to  6  in  steps  of   1  i.e.  20  , 25 , 30 , 35 , 40
print(*a[ : : -1])  #  *a[-1 : -9 : -1]    --->  Elements  of  object  'a'  from  indexes   -1   to  -8  in  steps  of   -1  i.e.   45  <space>  40  <space>  35  <space>  30  <space>  25 <space>  20  <space>  15  <space>  10 
#a[4] = 32 #  Error  becoz  range object can  not  be  modified
#print(a * 2)  #  Error  becoz range  object can  not  be  repeated 


'''
				                 0       1       2       3      4         5      6       7
range  object   --->  10     15     20      25    30      35    40     45
					           -8      -7     -6       -5     -4       -3     -2      -1
'''

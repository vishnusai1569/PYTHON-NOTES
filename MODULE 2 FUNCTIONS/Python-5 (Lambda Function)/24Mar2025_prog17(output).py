# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))  #   Nested  tuple
print(max(a , key = lambda  x  :  x[0] )) # (25 , 'Kiran' , 1500.0)
print(max(a , key = lambda  x  :  x[1] )) # (15 , 'Vamsi' , 2000.0)
print(max(a , key = lambda  x  :  x[2] )) # (20 , 'Sita' , 2800.0)
print(max(a)) # (25 , 'Kiran' , 1500.0)


# key  is  argument  of  max()  function  and  default  key  is  1st  element  of  each  inner  tuple

# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) # print(lambda  x : x ** 3)  ---> Type and address of lamba function x**3
print(a[key](5)) #5**3= 125



'''
1) What  are  the  keys  of  dictionary ?  --->  Strings
    What  are  the  values  of  dictionary ?  ---> Lambda  functions

2) key = 'power_3'
    What  is  the  result  of  a[key] ? ---> That  lambda  function  which  corresponds  to  'power_3'
                                                                i.e.  lambda   x :  x  **  3
'''

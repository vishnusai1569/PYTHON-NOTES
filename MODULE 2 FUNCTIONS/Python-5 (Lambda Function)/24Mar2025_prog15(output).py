# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0)) #  Nested  tuple
b = sorted(a) #  Sorts  tuple  'a'  based  on  1st  element  of  each  inner  tuple
print(b)  #  [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
c = sorted(a , reverse = True)  #  Sorts  tuple  'a'  based  on  1st  element  of  each  inner  tuple  in  descending  order
print(c) #  [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])  #  Sorts  tuple  'a'  based  on    2nd  element  of  each  inner  tuple due  to  x[1]
print(d)  # [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2])  #  Sorts  tuple  'a'  based  on    3rd  element  of  each  inner  tuple due  to  x[2]
print(e) # [(15 ,'Rajesh' , 500.0) , (10 , 'Rama' , 1000.0), (5 , 'Amar' , 1300.0) ,(20 , 'Sita' , 2000.0) , (18 , 'Kiran' , 2800.0) ]
print()
f = sorted(a , key = lambda   x  :  x[0])  #  Sorts  tuple  'a'  based  on    1st  element  of  each  inner  tuple due  to  x[0]
print(f) # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True) # Sorts  tuple  'a'  based  on    2nd  element  of  each  inner  tuple due  to  x[1] in descending order
print(g) # [(20, 'Sita', 2000.0),(10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0) ]
#print(sorted(a , key = x[1])) # error :  'x'  does  not  exist




'''
1) What  does  sorted()  function  return ?  --->  List  of  tuples

2) What  are  key  and  reverse  called ?  --->  Arguments  of  sorted()  function

3) How  to  sort  on  2nd  element (or) 3rd  element  of  each  inner  tuple ?  ---> With  key =  lambda  function

4) Is  lambda  function  required  to  sort  on  first  element ?  --->  No  becoz  default  key  is  first  element

5) What  is  the  alternative  to  sorted(a) ?  --->  sorted(a , key = lambda  x :  x[0])

6) sorted(a , key = lambda  x :  x[0])
    What  is  value  of  'x'  in  lambda  function ?  --->	Each  tuple  of   tuple  'a'
    What  is  x[0] ? ---> 1st  element  of   each   inner  tuple
    What  is  x[1] ? --->	2nd  element  of   each   inner  tuple
    What  is  x[2] ? --->	3rd  element  of  each   inner  tuple

7) sorted(a ,  key =  lambda   x  :  x[1])
    How  to  sort  using  regular  function ?  --->  print(sorted(a , key = f1))
    How  to  define  f1  function ?  ---> 	def   f1(x):
					     										  return  x[1]
'''

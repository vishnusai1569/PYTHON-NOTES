# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys()) #  Keys  are  sorted
print(b) # [5 , 10 , 15 , 18 , 20]
c = sorted(a . values()) #  Values  are  sorted
print(c) # ['Blue' , 'Green' , 'Red' , 'White' , 'Yellow']
d = sorted(a . items()) #   Tuples   are  sorted  based  on   1st  element
print(d) # [(5 ,  'White') , (10 , 'Red') , (15 , 'Blue') , (18 , 'Yellow') , (20 , 'Green')]
f  = sorted(a  , reverse = True)   #  Keys  are  sorted  in descending  order
print(f) # [20 , 18 , 15 , 10 , 5]
print(a) # {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}



'''
1) What  is  the  alternative  to  sorted(a . keys())  ?  --->  sorted(a)

2) sorted()  function  always  returns  list  irrespective  of  argument
'''

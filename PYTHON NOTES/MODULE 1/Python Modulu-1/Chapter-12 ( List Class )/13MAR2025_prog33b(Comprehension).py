'''
Repeat  previous  program  with  comprehension
i.e.  1 ^ 2 , 2 ^ 2 , 3 ^ 2 , .... 10 ^ 2
'''
a = [x **  2   for  x  in   range(1 , 11)]  # Appends  x  ^ 2  to  list  'a' where  'x'  varies  from  1  to  10
print(a)
print(type(a))  #  <class  'list'>

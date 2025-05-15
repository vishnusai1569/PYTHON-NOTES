# Write  a  program  to  create  a  list  with  1 ^ 2 , 2 ^ 2 , 3 ^ 2 , .....10 ^ 2  wihtout  comprehension
a = []
for  x  in   range(1 , 11):
	a . append(x ** 2)  #  Appends  x  ^ 2   to  list  'a'  where  'x'  varies  from  1   to  10
print(a)#   [1 , 4 , 9 , ..... , 100]


'''
    x       list   'a'
-------------------------------------
                []
    1          [1]
    2          [1 , 4]
    3          [1 , 4 , 9]
    4          [1 , 4 , 9 , 16]
    ....
    10         [1 , 4 , 9 , 16 , ...... , 100]
'''

# Tuple  Comprehension
g = (x * x   for   x   in   range(5))#   Creates  an  empty  generator  object
print(type(g)) #  <class  'generator'>
print(g) #  __str__()  method  returns  type  and  address  of  object  'a'
print(*g)  #  Unpacks  generator  object  to  0 ^ 2  <space>  1 ^ 2  <space> 2 ^ 2  <space> 3 ^ 2  <space>  4 ^ 2



'''
1) What  is  (x * x  for  x  in  range(5))  called ? --->  Generator  expression  but  not  tuple  comprehension

2) What  does  (x * x  for  x  in  range(5))  do ?  --->  Creates  an  empty  generator  object  but  not  tuple  with
														                            0  ^ 2 ,  1 ^ 2 , 2 ^ 2 , 3 ^ 2  and  4  ^ 2
'''

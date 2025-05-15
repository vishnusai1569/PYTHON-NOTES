'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  --->  [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17

Hint:  Use  map
'''
a = eval(input('Enter  first  list :  '))
b = eval(input('Enter  second  list :  '))
m = map(lambda  x , y : x * y , a , b)
print('Multiplication  list :  ' , list(m))
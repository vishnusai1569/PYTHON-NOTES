'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->   (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
a = eval(input('Enter  first  tuple :  '))
b = eval(input('Enter  second  tuple :  '))
m = map(lambda   x ,  y  : x + y , a , b)
print('Addition  tuple  :  ' , tuple(m))



'''
Let   tuple  'a'  be  (10 , 20 , 15 , 18)   and  tuple  'b'  be  (30 , 40 , 35 , 12 , 19 , 17)

1)   x       y      x  +  y       map  obj  'm'
    ---------------------------------------------------
     10     30        40                 40
     20     40        60                 40  , 60
     15     35         50                 40  , 60 , 50
     18     12          30                 40  , 60 , 50 , 30

2) m = map(lambda   x ,  y  : x + y , a , b)
    What  is  'x'  ?  --->	Each  element  of  tuple  'a'
    What  is  'y'  ?  --->  Each  element  of  tuple  'b'

3) Where  is  x +  y  returned  to ?  --->  Map  object  'm'

4) What  does  tuple(m)  do ?  --->  Stores  all  the  results  in  map  object  'm'  and  converts  to  tuple

5) Excess  elements  of  either  tuple  are  ignored

6) How  to  define  regular  function  instead  of  lambda  function ?  --->  def   add(x , y):
																															return  x + y

7) How  to  create  map  object  with  regular  function ?  --->  m = map(add , a , b)
'''
# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x)
	print(type(x))

'''
[10 , 20]
<class 'list'>
{30 , 40 , 50} can be any order
<class 'set'>
(60  , 70 , 80 , 90)
<class 'tuple'>
100
<class 'int'>
'''


'''
1) What  does  generator  yield  for  the  1st  time ?  ---> [10 , 20]

2) What  does  generator  yield  for  the  2nd  time ?  ---> {30 , 40 , 50}

3) What  does  generator  yield  for  the  3rd  time ?  ---> (60, 70 , 80 , 90)

4) What  does  generator  yield  for  the  4th   time ?  --->  integer  100

5) What  does  generator  yield  for  the  5th   time ?  --->  Throws  StopIteration  error  as  nothing  is  yielded
'''

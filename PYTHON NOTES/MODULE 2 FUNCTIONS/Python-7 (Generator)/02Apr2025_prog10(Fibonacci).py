'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  ---> 0  and  1

4) Use  generator  function  and  for  loop
'''
import  time
def  fib(x):
	a = 0
	yield  a
	b = 1
	yield  b
	c = a + b
	while c <=  x:
		yield  c  #   2
		a = b
		b = c
		c = a + b
# End  of  generator  function
x = int(input('What  is  the  last  value  :  '))
g = fib(x)
for  k  in  g:
	print(k)
	if  x == 0:
		break
	time . sleep(2)







'''
1) What  is  the  issue  with  yield  a := 0 ?  --->


Yield  is  executed  before  walrus  operator  due  to  higher  priority

2) What  is  the  issue  with  while  c := a + b <= x ?  --->


<=  is  executed  before  walrus  operator  due  to  higher  priority
'''

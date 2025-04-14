'''
Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , ....

2) What  is  the  formula  for  10th  term ?  --->  9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term

3) What  are  the  first   two  terms ?  --->  0  and  1
'''
def  fib(i):  #  'i'  is  term  number
	if  i == 1:
		return   0
	if  i == 2:
		return  1
	return  fib(i - 1) + fib(i - 2)
'''
fib(5) = fib(4) + fib(3)
          = fib(3) + fib(2) + fib(2) + fib(1)
          = fib(2) + fib(1) + 1 + 1 + 0
          = 1 + 0 + 1 + 1 + 0
          = 3

fib(4) = fib(3) + fib(2)
          = fib(2) + fib(1)
  Function  call     Number  of  Function  calls        Result
  -------------------------------------------------------------------
       fib(1)                             1                                   0

	   fib(2)                            1                                    1

	   fib(3)                            3                                    1

	   fib(4)                            5                                    2

	   fib(5)                            9                                    3

	   fib(6)                            15                                   5

	   fib(7)                            25                                  8
'''
n = int(input('How many terms ? :  '))  #  5
print('Fibonacci  series')
for  i  in  range(1 , n + 1):  #How  to  print  first  'n'  terms  of  fibonacci  series
	print(fib(i))  #  0  ,  1  ,  1  ,  2 , 3



'''
1) What  does  fib(i)  generate ?  --->  ith  term  of  fibonacci  series

2) How  to  generate  fibonacci  series ?  --->  Call  fib()  function  'n'  times  in  the  for  loop
'''

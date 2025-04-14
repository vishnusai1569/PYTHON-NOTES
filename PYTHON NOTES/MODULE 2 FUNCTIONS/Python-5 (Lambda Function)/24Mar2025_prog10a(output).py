#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:  #   fun  is  each  lambda  function  of  list  'a'
        print(fun(5)) #25<next line>125<next line>625


'''
Does  list  contain  5 ^ 2 , 5 ^ 3  and  5 ^ 4 ?  --->  No  and  it  is  a  list  of   lambda  functions

	  Iteration              fun                                       fun(x)
	-------------------------------------------------------------------------------------
	     1             lambda  x : x  **   2           x  is   5  and  result is  25
	     2            lambda  x : x  **   3           x  is   5  and  result is  125
	     3            lambda  x : x  **   4           x  is   5  and  result is   625
'''

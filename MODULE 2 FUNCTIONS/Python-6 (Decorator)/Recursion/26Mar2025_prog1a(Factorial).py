# Write  a  recursive  function  for  factorial
#import sys
#sys.setrecursionlimit(2000)
def  fact(n):
	if  n > 0:
		return  n * fact(n - 1)
	else:
		return   1
'''
fact(4) = 4 * fact(3)
            = 4 * 3 * fact(2)
            = 4 * 3 * 2 * fact(1)
            = 4 * 3 * 2 * 1 * fact(0)
            = 4 * 3 * 2 * 1 * 1
			= 24
'''
n = int(input('Enter  any  +ve  integer  or  0  :  '))    #   4
print(F'{n}  !=  {fact(n)}')  #  How  to  print  n  and  n!)



'''
1) How  many  function  calls  are  in  fact(4) ?  --->  5
    How  many  times  is  fact()  function  called  from  ouside  the  function ?  ---> 	Just  once
    How  many  times  is  fact()  calling  itself ?  ---> Next  4  times

2) How  many  function  calls  are  in  fact(n) ?  --->  n + 1

3) def  fact(n):
		    return  n * fact(n - 1)
    What  is  the  result  of  fact(4) ?  --->  4 * fact(3)
																	=  4 * 3 * fact(2)
											  						=  4 * 3 * 2 * fact(1)
																	=  4 * 3 * 2 * 1 * fact(0)
																	=  4 * 3 * 2 * 1 * 0 * fact(-1)
																	=  4 * 3 * 2 * 1 * 0 * -1 * fact(-2)
																	and  so  on

4) In  other  words,  it  becomes  infinite  recursion

5) def  fact(n):
	     if  n > 0:
		     return  n * fact(n)
	     else:
		     return   1
    What  is  the  result  of  fact(4) ?  --->	4 * fact(4)
																    = 4 * 4 * fact(4)
																    = 4 * 4 * 4 * fact(4)
																    and  so  on

6) In  other  words,  it  becomes  infinite  recursion

7) def  fact(n):
	     if   n > 0:
		       return  fact(n - 1)
   	    else:
			   return   1
    What  is  the  result  of  fact(4) ?  ---> 	fact(3) = fact(2) = fact(1) = fact(0) = 1

8) In  other  words,  result  is  always  1  for  any  input

9) Can  if  conidition  be  changed  to  n == 0  ?  ---> Yes  provided  the  two  return  statements  are  interchanged
																			      Eg:  if  n  == 0:
																							 return   1
																						 else:
																							  return  n * fact(n - 1)
'''

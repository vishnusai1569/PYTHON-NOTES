'''
Write  a  program  to  write  0! ,  1! , 2!, ...... n!  to  the  file

Hint:  Use  math . factorial()  function
'''
import  math
def  fact(f , n):
	for  i  in  range(n + 1):
		f . write(F'{i}  !=  {math.factorial(i)}\n')  #  Writes   i  and  i!  to  the  file  where  'i'  varies  from  0  to  'n'
# End  of  the  function
fname = input('Enter filename : ') #  Reads  filename
f = open(fname , 'w')  #  Opens  file  in  write  mode
n = int(input('Enter  value  of  n : '))  #  Reads  value  of 'n'
fact(f , n) #  Writes  0! , 1! , 2! , ... n!  to  the  file
f . close()  #  Closes  the  file
print(F'View   {fname}  for  results')


'''
f . write(i , '!=' , math . factorial(i) , '\n')
Is  the  statement  valid   ?  --->  No  becoz  write()  method  takes  single  argument  but  not  4  arguments
'''
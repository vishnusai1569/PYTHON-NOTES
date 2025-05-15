'''
Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a(prime).py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime   numbers
																		   2
																		   3
																		   5
																		   7
																		   Number  of   prime  numbers : 4
'''
from  prog3a  import  prime   #  imports  prime()  function  and   if  statement
n = int(input('Enter  value  of  n  :  '))  #  How  to  read  a  number
ctr = 0
for  i  in  range(2 , n + 1): # How  to  print  all  prime  numbers  between  2  and  user  input
	if  prime(i):
		print(i)  #  2 , 3  ,  5 ,  7
		ctr += 1  #  4
print('Number  of  prime numbers  :  ' ,   ctr)



'''
1) py  prog3a.py
    What  is  the  value  of  __name__ variable ?  --->   '__main__'  becoz  prog3a  is  executed  directly

2) import  prog3a
    from  prog3a  import  prime
    What  is  the  value  of  __name__ variable ?  --->  Imported  module name  i.e.   'prog3a'

3) from  prog3a   import  prime
     Is  if  statement  imported  from  prog3a ?  ---> Yes  but  not  executed  becoz  condition  is  False

4) Who  is  initializing  __name__  and  when ? --->  PVM  automatically  initializes  __name__  variable  as  soon  as
																				  program  is  executed

5) What  is  the  type(__name__) ?  --->  <class  'str'>
'''

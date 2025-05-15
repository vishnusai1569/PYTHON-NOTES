#  Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)
def  avg(*a):
	#Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
	try:
		return sum(a)/len(a)
	except  ZeroDivisionError:
		return   0
	except  TypeError:
		return  sum(*a) / len(*a)
# End  of  the  function
print(avg(10 , 20 , 15 , 18))  #   Tuple  of   4  args is  passed  to  the  function  and   result   is   (10 + 20 + 15 + 18) / 4 = 15.75
print(avg(25 , 10.8 , True))   #   Tuple  of  3  args is  passed  to  the  function  and   result   is   (25 +10.8 + 1) / 3 = 12.26
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))   #   Tuple  of   5  args is  passed  to  the  function  and   result   is   (10.8 + 20.6 + 15.2 + 14.9 + 9.8) / 5 
print(avg())  #  Empty  tuple   is  passed  to  the  function  and   result   is  0
print(avg(25))   #   Tuple  of  sinlge  arg  is  passed  to  the  function  and   result   is   25 / 1 = 25.0
print(avg(3 + 4j , 5 + 6j))   #   Tuple  of   2  args is  passed  to  the  function  and   result   is   (3 + 4j + 5 + 6j) / 2 =  4 + 5j
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))   #  Nested  tuple  is  passed  to  the  function  and   result   is   (10 + 20 + 15 + 18) / 4 = 15.75




'''
1) a = (10 , 20 , 15,  18)
    What  is  sum(a)  ? --->	63
    What  is  len(a) ? --->  4

2) a = ((10 , 20 , 15,  18) , )
    What  is  sum(a) ? --->  0 + (10 , 20 , 15 , 18)  throws   TypeError  
    What  is  len(a) ? --->  1

3) a = ((10 , 20 , 15,  18) , )
    What  are  the  two  ways  to  obtain  inner  tuple  from  tuple  'a'  ?  --->  a[0]  and  *a

4) a = ((10 , 20 , 15,  18) , )
    What  is  a[0] ?  --->  (10 , 20 , 15 , 18)
    What  is  sum(a[0]) ? ---> 	63
    What  is  len(a[0]) ? --->  4

5) a = ((10 , 20 , 15,  18) , )
    What  does  *a  do  ?  --->  Unpacks  outer  tuple  to  obtain  inner  tuple  i.e.  (10 , 20 , 15 , 18)
    What  is  sum(*a) ?  ---> 63
    What  is  len(*a) ?  ---> 4

6) What  does  0 / 0  do  ?  --->  Throws  ZeroDivisonError
'''

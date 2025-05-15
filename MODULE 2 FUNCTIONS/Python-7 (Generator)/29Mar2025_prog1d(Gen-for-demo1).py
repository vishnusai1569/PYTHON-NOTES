#  How  to  iterate  generator  with  for  loop
import  time
def   f1():#   Generator  function  due  to  yield
	print('One')
	yield  25  #   25  is   returned  to  for  loop  variable  'x'
	print('Two')
	yield  10.8  #    10.8  is   returned  to  for  loop  variable  'x'
	print('Three')
	yield  'Hyd'   #   'Hyd'   is   returned  to  for  loop  variable  'x'
	print('Four')
# End  of  generator
g = f1()  #  Creates  an  empty  generator  object
for   x   in   g:
	print(x)
	time . sleep(1)
	print('Hello')
#  End  of  for  loop
print('End')
print(g)   #  __str__()  method   returns  type  and  address  of  object  'g'
#print(next(g))    #  Throws  StopIteration  Error
g = f1()    #   Creates  another  generator  object
print(next(g))  #  Yields  25


'''
One
25
Hello
Two
10.8
Hello
Three
Hyd
Hello
Four
End
<generator object f1 at 0x00000238C5765F00>
One
25
'''



'''
1) What  are  the  two  ways  to  iterate  a  generator ?  --->  next(g)  in  while  loop
																								    and
																								 for  loop

2) How  to  iterate  a  sequence ?  --->  With  for  loop  only

3) Is  next(sequence)  valid ?  --->  No  becoz  argument  should  be  generator  but  not  sequence

4) Which  is  a  better  approach (for  loop  (or)  next()  function )  to  iterate  a  generator ?  --->									
														for  loop   becoz  StopIteration  error  is  internally  handled  by  for  loop

5) How  long  is  for  loop  executed ?  --->  Until  StopIteration  error  is  raised

6) How  many  times  can  generator  be  iterated ?  --->  Only  once
    How  many  times  can  a   sequence  be  iterated ?  --->  Multiple  times

7) for  x  in   generator:
	      statements
    for  x  in   same  generator:
	      statements
    for  x  in   same  generator:
	      statements
    Are  2nd  and  3rd  for  loop  execucted ?  --->  No  becoz  StopIteration  is   raised  in   the  1st  iteration  itself
																			   as  generator  is  already  fully  iterated  after  1st  for  loop

8) for  x  in   sequence:
	      statements
    for  x  in   same  sequence:
	      statements
    for  x  in   same  sequence:
	      statements
    Are  2nd  and  3rd  for  loop  execucted ?  --->  Yes  becoz  sequence  can  be  iterated  multiple  times
'''

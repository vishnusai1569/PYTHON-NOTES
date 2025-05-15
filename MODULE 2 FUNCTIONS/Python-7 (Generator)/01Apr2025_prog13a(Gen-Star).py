# How  to  access  generator  object   with  *  operator ?
def   f1():
	print('One')
	yield  25
	print('Two')
	yield  10.8
	print('Three')
	yield  'Hyd'
	print('Four')
# End of  generator
g = f1() #   Creates  an  empty  generator  object
print('Begin')  # Begin
print(*g)
print('End')

'''
Begin
One
Two
Three
Four
25 10.8 Hyd
End
'''


'''
1) What  are  the  three  events  in  execution  of  *g  ?  --->
	a) Generator  function  is  fully  executed  without  stopping  in  the  middle  even  though  there  is  yield  statement
	b) All  the  elements  yielded  by  generator  function  are  stored  in  generator   object  'g' (non-empty  object)
	c) Generator  object  is  unpacked  due  to  *  operator  until  StopIteration  error  is  raised

2) Do  we  need  to  handle  StopIteration  error ?  --->  No  and  it  is  internally  handled  by  *  operator

3) What  are  the  two  drawbacks  of  *g ?   --->  a) Waiting  time  when  there  are  too  many  yield  statements
																			   b)  Possibility  of  MemoryError

4) Hence  *g  is  not  recommened  for  generator  as   we  are  losing  the  power  of  generator

5) Therefore  for  loop  (or)  next(g)  is  preferred  for  generator
'''

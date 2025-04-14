# Find  outputs  (Home  work)
def   f1(begin , end):
	while  begin  <=  end:
			print('Hello')
			yield  begin
			begin += 1
	print('End  of  generator')
#end of the genrator  function
g = f1(10 , 20)  #  Creates  an  empty  gen  object
print('Before')
print(list(g))
print('After')
#print(next(g))  #  StopIteration  error : Gen  is   fully iterated

'''
Before
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
End  of  generator
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
After
'''




'''
1) What  are  the  three  events  for  list(g) ?  --->
	a) generator  function  is  fully  executed  without  stoping  in  the  middle  even  though  there  is  yield  statement
	b) All  those  elements  which  are  yielded  are  stored  in  generator  object  (non-empty  object)
	c) generator  object  is  converted  to  list  until  StopIteraton  error  is  raised

2) What  are  the  two  drawbacks  of  list(g) ?  ---> a) Waiting  time  when  there  are  too  many  yield  statements
																				  b)  Possibility  of  MemoryError

3) Hence  list(g)  is  not  recommended  for  generator  as  we  are  losing   the  power  of  generator
'''

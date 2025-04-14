#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for  y  in   g:   #  Not  executed  becoz  object  'g'  is   fully  iterated
	print(y)



'''
0
<2 seconds>
Hello
1
<2 seconds>
Hello
4
<2 seconds>
Hello
9
<2 seconds>
Hello
16
<2 seconds>
Hello
'''


'''
1) How  many  times  can  a  generator  object  be  iterated ?  --->  Just  once
    What  about  sequence ?  --->  It  can  be  iterated  multiple  times

2) g = (x * x   for    x    in    range(5))
    for   y  in   g:
	      pass
    for   y  in   g:
	      pass
    Why  is  2nd  for  loop  not  executed ?  --->  Since  StopIteration  error  is  thrown  in  1st  iteration  itself
'''

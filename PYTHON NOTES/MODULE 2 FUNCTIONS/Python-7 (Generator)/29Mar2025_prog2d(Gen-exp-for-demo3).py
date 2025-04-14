# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))   #   g1  points  to  new  gen  object
g2 = g1   #  g2 points  to  same  gen  object  g1
for  y  in  g1:
	print(y)
	time . sleep(2)
for  y  in  g2:   #  Not  executed  becoz  g2  (i.e. g1)  is  fully  iterated
	print(y)
print(g1  is  g2) # True as g1 and g2 has same generator object



'''
0
<2 seconds>
1
<2 seconds>
4
<2 seconds>
9
<2 seconds>
16
<2 seconds>
True
'''


'''
1) How  many  generator  objects  are  in  the  program ?  --->  Just  one  object  with  two  references  g1  and  g2

2) Why  is  2nd  for  loop  not  executed ?  --->  Since  it  is  already  fully  iterated  and  throws  StopIteration  error
																			in  1st  iteration  itself

3) How  many  times  can  a  generator  object  be  iterated ?  --->  Just  once
'''

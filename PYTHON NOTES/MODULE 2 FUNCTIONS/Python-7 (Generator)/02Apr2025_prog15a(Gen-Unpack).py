#  Find    outputs (Home  work)
def      f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1() #  Creates  an  empty  generator  object
for   m   in   g: #   Iteraates  object  'g'
	print(m)
x ,  y ,  z  =  f1()   #  3  events
print(x)
print(y)
print(z)

'''
One
1
Two
2
Three
3
End
One
Two
Three
End
1 
2 
3
'''

'''
1) What  are  the  three  events  for  x , y , z = f1() ?  --->
	a) generator  function  is  fully  executed  without  stoping  in  the  middle  even  though  there  is  yield  statement
        Outputs  are   One , Two , Three , End     
   b) Elements  yielded  by  generator  are  stored  in  object  'g'
       i.e.  1 , 2 , 3 
   c) generator  object  is  unpacked  into  objects  x , y  and  z

2) What  are  the  two  drawbacks  of  unpacking  generator ?  --->  Waiting  time  and  MemoryError

3) x  =  f1()
    x , y , z = f1()
    What  is  the  difference  between  the  above  two  statements ?   --->	 
	 a)  x  = f1()  creates  an  empty  generator  object
	 b)  x , y , z = f1()  creates  a  generator  object  with  three  elements  which  is  unpacked
'''

# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):  #  Iterates  1st  generator  object
	print(y)
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):  #  Iterates  2nd   generator  object
	print(y)
	time . sleep(2)



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


0
<2 seconds>
1
<2 seconds>
4
<2 seconds>
9
<2 seconds>
16
'''


'''
1) How  many  generator  objects  are  in  the  program ?  --->  2

2) When  is  generator  object  created ?  --->  As  soon  as  generator  expression  is  reached

3) How  to  iterate  generator  object  ?  --->  Either  next(gen-object)
																					  (or)
															            for   x  in   gen-object:
'''

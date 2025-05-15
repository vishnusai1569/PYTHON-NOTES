# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):  #  x  and  y  are  elements  of  each  tuple  yielded  by   zip  iterator
	print(x + y)  #   5  <next  line>  7  <next  line>  9  <next  line>
	time . sleep(1)


'''
1)      Iteration    x      y    x + y
        -----------------------------------------
                  1        1       4       5
                  2        2      5       7
                  3        3      6       9

2) What  happens  to  elements  7  and  8  ?  --->  Ignored  becoz  they  are  excess  elements  and  throws  StopIteration  error
'''
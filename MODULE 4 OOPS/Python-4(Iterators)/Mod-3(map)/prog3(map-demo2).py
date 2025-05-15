# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a) #  Creates  an  empty  map  object
while   True:
	try:
		print(next(m))  #   10  <next  line>  20  <next  line>  15  <next  line>  5  <next  line>  18 <next  line>
		time . sleep(1)
	except  StopIteration:
		break

'''
       x              x[1]             next(m)
-------------------------------------------------
('A' , 10)         10                   10

('B' , 20)         20                  20

('C' , 15)          15                  15

('D' , 5)            5                   5

('E' , 18)           18                 18
'''
'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  46 , 34.8 , False , 95 , -1

sum = 0 + 25 + 10.8 + True + 46 + 34.8 + False + 95

ctr = 0  + 1 + 1 + 1 + 1 + 1 + 1 + 1
'''
try:
	sum =  ctr = 0
	x = eval(input('Enter input  (-1  to  stop)  :  '))  #   'Ten'
	while  x != -1:
		sum += x  #  sum = 0 + 25 + 10.8 + 1 + 46 + 34.8 + 0 + 95
		ctr +=1 #  ctr = 0 + 1 + 1 + 1 + 1 + 1 + 1 + 1
		x = eval(input('Enter input  (-1  to  stop)  :  '))  #   -1
		break
	# End  of  while  loop
	print('Average :  ' ,  sum / ctr)
except  ZeroDivisionError:
	print('1st  input  can  not  be  -1')
except (TypeError , NameError):
	print('Input  can  not  be  string')

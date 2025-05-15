'''
Modify  following   program  with  walrus  operator
Hint:  Combine  lines  7 , 8   and  11  to a  single  line  with   walrus  operator
'''
try:
	sum =  ctr = 0
	while  (x := eval(input('Enter any  number  (ctrl+z  to  stop) : ')))  != -1:
		sum += x  #  sum = 0 + 10 + 20 + 15 + 18
		ctr +=1   #  ctr = 0 + 1 + 1 + 1 + 1
	# End  of  while  loop
	print('Average :  ' ,  sum / ctr)
except  (NameError , TypeError):
	print('Input  can  not  be string')
except  ZeroDivisionError:
		print('Enter  at  least   one  input')


'''
1) while  x := eval(input())  !=   -1:
    What  is  the  issue  with  above  while  loop ?  --->  !=   is  evaluated  before  :=  due  to  higher  priority

2) Hence  brackets  are  mandatory  for  walrus  operator (:=)

3) What  is  ctrl+z ?  --->  End  of  inputs

4) What does  input()  do  when  input  is  ctrl+z ?  --->  Throws   EOFError

5) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d
'''

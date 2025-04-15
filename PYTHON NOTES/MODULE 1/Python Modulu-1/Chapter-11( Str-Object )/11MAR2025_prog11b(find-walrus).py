'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = -1
while  (index := a . find('is' , index + 1))  != -1:
	print(index)  #  4 , 23 , 42 , 46
print('End')  #  End



'''
while   index  :=   a . find('is' , index + 1)   !=   -1:
What  is   the   issue  with  the  above  while  condition ? --->   !=  is  evaluated  before  :=   due  to  higher  priority
                                                                                                  and  leads  to  infinite  loop
'''

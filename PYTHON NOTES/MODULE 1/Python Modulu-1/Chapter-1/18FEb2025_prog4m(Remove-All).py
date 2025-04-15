'''
Write  a  program  to  remove  all  15's  from  the  list

Hint:  while  cond:
		          statements
          statements
'''
a = [10 , 20 , 15 , 18 , 12 , 15 , 19 , 25 , 15 , 14 , 12]
while   15  in   a:    # Repeat  until  there  is  no  15  in  the  list:
		a . remove(15)  #  How  to  remove  each  15  from  the  list
print(a)   #   [10 , 20 , 18 , 12 , 19 , 25 ,  14 , 12]


'''
How  to  remove  each  15  from  the  list ?  --->  Call  remove()  method  in  a  loop
'''

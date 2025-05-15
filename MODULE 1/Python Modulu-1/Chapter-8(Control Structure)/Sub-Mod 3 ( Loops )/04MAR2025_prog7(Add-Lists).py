'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
for  i   in   range(len(a)):  #  How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
		c . append(a[i] + b[i])
print('3rd  list : ' , c)
#   How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop  --->  Not  possible



'''
1) c = []
    for  x , y  in  a , b:
	     c . append(x + y)
    What  is  the  issue  with  the  above  for  loop ?  ---> Two  sequences  are  not  permitted  in  for  each  loop

2) for  each  loop  can  iterate  one  sequence  at  a  time  but  not  multiple  sequences  simultaneously

3) a = [10 , 20 , 15 , 18]
    b  = [30 , 40 , 35 , 12]
    What  is  the  result  of  a + b ?  ---> [10 , 20 , 15 , 18 , 30 , 40 , 35 , 12]
										                       i.e.  List  of  8  elements

4) Finally  what  does  a + b  do ?  --->  Concatenates  lists  a  and  b  but  does  not  add  them
'''

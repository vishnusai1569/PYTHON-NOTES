 #index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')

'''
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times
'''


'''
1) Can  break  be  used  in  except  suite ?  ---> No  becoz  except  suite  is  outside  the  loop

2) a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
    i = a . index(100)
    try:
	    while  True:
		    print('100  is found at index : ' , i)
		    i = a . index(100 , i + 1)
    except:
	     print(F'100  is  found  {a . count(100)}  times')
    Is  except  suite  executed  for  a . index(100) ?  --->	No  becoz  it  is  not  in  try  suite  and  reports  error
'''

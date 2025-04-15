# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list)  #   [10,20,18,15,12,15,19]
	list . remove(25)  #  Error
except:
	print('25  is   not  in  the  list')  #  25  is  not  in  the  list



'''
remove()   method
---------------------
1) What  does  remove(x)  do ?  --->  Removes   first  occurance  of  'x'  from  the  list

2) What  does  remove()  method  do  if  'x'  is  not   in  the  list ?  ---> Throws  ValueError

3) Does  remove(x)  delete  all  ocurances  of  'x'  from  the  list ?  --->  No  and  only  first  occurance  of  'x'  is  removed
'''

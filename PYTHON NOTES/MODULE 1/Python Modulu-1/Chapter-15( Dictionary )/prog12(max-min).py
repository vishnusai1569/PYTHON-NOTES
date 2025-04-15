# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) #  Largest  key  i.e. 40
print(min(a . keys())) #  Smallest  key  i.e.  7
print(max(a . values())) #  Largest  value  i.e.  50
print(min(a . values())) #  Smallest  value  i.e.  5
print(max(a . items())) #  The  tuple  with  largest  first  element  i.e.  (40 , 5)
print(min(a . items()))   #  The  tuple  with  smallest  first  element  i.e.  (7 , 28)
print(max(a)) #  Largest  key  i.e. 40
print(min(a))  #  Smallest  key  i.e.  7



'''
1) What  is  the  alternative  to  max(a . keys()) ?  --->   max(a)

2) What  does  items()  method  return ? ---> dict_items([(10 , 20) , (30 , 25) , (40 , 5) , (7 , 28) , (9 , 50)])
'''

# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)  #  {'Hyd' , 25 , 10.8 , True}  in  any  order
print('Iterate  elements  of  set  with  for  loop')
for x in a :  # How  to  iterate  set  with  for  loop
	print(x)  #  Hyd  <next  line>25  <next  line>  10.8  <next  line>  True  <next  line>


'''
1) set  is  iterated  in  the  same  order  in  which  it  is  printed  becoz  it  is  the  same  set

2) a = {25 , True , 'Hyd' , 10.8}
    for  i   in   range(len(a)):
	     print(a[i])
    Is  the  above  for  loop  valid ?  --->  No  becoz  set  is   not  indexed

3) Therefore  use  for  each  loop  to  iterate  set  but  not  indexed  based  for  loop
'''

# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)#   Returns  a  sorted  list
print(b)   #  [5 , 10 , 12 , 15 , 20]
print(type(b)) #  <class  'list'>
c = sorted(a , reverse = True)  #  Returns  a  sorted  list  in  descending  order
print(c)  #  [20 , 15 , 12 , 10 , 5]
print(a) #  [10 , 20 , 15 , 5 , 12]


'''
sorted()  function
----------------------
1) What  does  sorted(list)  do  ?  ---> Returns  another  sorted  list

2) Is  argument  list  modified ?  --->  No  and  it  remains  unchanged

3) How  to  sort  list  in  descending  order ?  --->  sorted(list , reverse = True)

4) What  are  the  two  arguments  of  sorted()  function ?  --->  List  to  be  sorted
																												and
																					                 reverse = True  which  is  an  optional  argument
'''

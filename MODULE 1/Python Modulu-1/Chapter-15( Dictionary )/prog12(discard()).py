# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  #{25 , 10.8 , 'Hyd' , True} can be any order
a . discard('Hyd')  #  Removes  'Hyd'  from  set  'a'
print(a) # {25 , 10.8 , True} can be any order
a . discard('Sec')  #No  error  even  though  'Sec'  is  not  in  set  'a'
print(a)  #  {25 , 10.8 , True} can be any order
#a . remove('Sec') # error as there is no 'Sec' in the set


'''
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) Does  discard(Invalid  element)  throw  error ?  ---> No
'''

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #  {25 , 10.8 , 'Hyd' , True}  in  any  order
a . discard('Hyd')  #Removes  'Hyd'  from set  'a'
print(a)  #  {25 , 10.8 , True}  in  same  order  (same as  line  3)
a . discard('Sec')  #  No  error  due to  discard()  method
print(a) #   {25 , 10.8 , True}  in  same  order  (same as  line  3)
#a . remove('Sec')  # Error  : There  is no  'Sec'  in  set  'a'


'''
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) Does  discard(Invalid  element)  throw  error ?  --->  No
'''

# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))  #  True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))  #  False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) #  False  due  to  empty  string
d = [10 , 0 , 20]
print(all(d)) #  False  due to  0
e = []
print(all(e))  #  True  becoz  there  are  no  false  elements    in  list  'e'



'''
all()  function
-----------------
1) What  does  all(list)  do ?  --->  Returns  True  when  every  element of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  at  least  one  element  of  the  list  is  False

3) if  cond1  and  cond2  and  cond3  and  cond4:
    How  to  reduce  the  above  four  conditions  to  a  single  condition ?  --->  if  all([cond1 , cond2 , cond3 , cond4]):
'''

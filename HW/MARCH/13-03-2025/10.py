# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)#[10 , 20 , 15 , 18]
print(a  is  b)#False
print(a  ==  b)#True
c = a[:]
print(c)#[10 , 20 , 15 , 18]
print(a  is  c)#False
print(a  ==  c)#True
d = a
print(d)#[10 , 20 , 15 , 18]
print(a  is  d)#True
print(a  ==  d)#True



'''
copy()  method
------------------
1) What  does  copy()  method  do ? --->  Copies  elements  of  list  to  another  list  and  returns  the  new  list

2) b = a . copy()
    What  is  another  way  to  copy  list  elements  to  another list ?  --->  b = a[:]
'''
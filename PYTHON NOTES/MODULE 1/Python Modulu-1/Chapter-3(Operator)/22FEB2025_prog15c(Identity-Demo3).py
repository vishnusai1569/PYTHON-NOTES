# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b)  #   True
print(a  is  not  b)  #   False
print(a == b)  #  True  due  to same  strins
print()
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)  #  False
print(x  is  not  y) #   True
print(x == y) #  True
print()
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)  #  True
print(m  is  not  n) #  False
print(m == n)  #  True
print(x == m) #   False becoz  x  and  m  point  to  different  objects


'''
list == tuple
What  does  ==  do ?  --->   Compares   references  but  not  objects  becoz  they  are  different  class  objects
'''

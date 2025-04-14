# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)  #  'a'  is  10 , 'b'  is  7  , result  is   x =  (17 , 3 , 70 , 1.42)
print(type(x)) # <class 'tuple'>
print(x) #(17 , 3 , 70 , 1.42857 )
p , q , r , s = all(9 , 2)  #  p , q , r , s = (11 , 7 , 18 , 4.5)
print(p) # 11
print(q) # 7
print(r) # 18
print(s) # 4.5

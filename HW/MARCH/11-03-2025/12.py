# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list
print('x : ' , x)#25
print('y : ' , y)#[10.8,hyd,True]
*p , q = list
print('p : ' , p)#[25, 10.8, 'Hyd']
print('q : ' , q)#True

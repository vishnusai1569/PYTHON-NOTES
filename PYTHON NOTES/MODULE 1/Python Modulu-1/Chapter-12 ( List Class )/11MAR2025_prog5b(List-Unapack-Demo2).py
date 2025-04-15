# Find  outputs
list = [25 , 10.8 , 'Hyd' , True]
a ,  b , *c = list  #  Unpacks  list  into  3  objects
print('a : ' , a) #  a : 25
print('b : ' , b) #  b : 10.8
print('c : ' , c) #  c : ['Hyd' , True]
print(type(c))#   <class  'list'>

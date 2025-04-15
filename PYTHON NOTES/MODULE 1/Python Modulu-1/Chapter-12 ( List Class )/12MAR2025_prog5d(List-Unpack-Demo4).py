# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list  #  Error due  to  few elements  in  the  list
a , b , *c , d , e = list
print('a : ' , a)  #   a :  25
print('b : ' , b)  # b : 10.8
print('c : ' , c) #  c : []
print('d : ' , d)  # d : Hyd
print('e : ' , e) #  e : True
#a , b , *c , d , e , f = list   #  Error due  to  few elements  in  the  list

# List  unpacking
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d = list  #  Unpacks  list  into  4  objects
print('a : ' , a) #   a: 25
print('b : ' , b) #  b : 10.8
print('c : ' , c) #  c : Hyd
print('d : ' , d) #  d : True
#x , y , z = list  #  Error  due to  excess  elements  in  the  list
#a , b , c , d , e = list   #  Error  due  to  few  elements  in  the  list


'''
1) What  is  list  packing  ? --->  Joins  multiple  objects  to  form  a  new  list
								                  Eg:  [obj1 , obj2 , obj3 , ......]

2) What  is  list  unpacking ?  --->  Divides  list  into  multiple  objects
													  Eg:  obj1 , obj2 , obj3 , ....  =  list
'''

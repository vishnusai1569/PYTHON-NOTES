# Find  output (Home  work)
add = lambda  x , y : x + y #How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add)) # <class 'function'>
print(add(10 , 20)) #  'x'  is  10 ,  'y'  is  20  and  result  is  30
print(add(10.6 , 20.8)) #  'x'  is  10.6 ,  'y'  is  20.8  and  result  is  31.4
print(add('Hyder' , 'abad')) #  'x'  is  'Hyder' ,  'y'  is   'abad'  and  result  is   'Hyderabad'
print(add(True , False))  #  'x'  is   True ,  'y'  is  False  and  result  is   1
print(add(25 , 10.8))  #  'x'  is  25 ,  'y'  is   10.8  and  result  is   35.8
print(add(3 + 4j , 5 + 6j))  #  'x'  is  3 + 4j ,  'y'  is   5 + 6j  and  result  is  8 + 10j
#print(add(10 , '20')) # #  'x'  is  10 ,  'y'  is  '20'  and  10 + '20'  throws  error
#print(add()) #Error :  Arguments  are  not  passed  for  'x'  and  'y'
print(add) #  type and address of lamda function



'''
add = lambda  a , b : a + b
How  to  define  regular  function  instead  of  lambda  function  ?  --->  def  add(a , b):
																													    return   a + b
'''

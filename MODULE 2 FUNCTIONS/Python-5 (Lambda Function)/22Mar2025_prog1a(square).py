# Lambda  function  to  find  square  of  a  number
square = lambda x :  x * x  #   Ref  square  points  to  lambda  function
print(type(square))#   <class  'function'>
print(id(square))  # Address  of  lambda  function
print(square(5))   #  'x'  is   5  and  result  is  25
print(square(2.5))  #  'x'  is   2.5  and  result  is  6.25
print(square(True))  #  'x'  is    True   and  result  is  1
print(square(3 + 4j))  #  'x'  is   3 + 4j  and  result  is  (3 + 4j) * (3 + 4j) = -7 + 24j
#print(square())  #  Error :  Arg  is  not  passed  for  'x'
print(square)  #  Type  and  address  of  lambda  function



'''
1) square =  lambda  x  :   return   x * x
    Is  the  above  lambda  function  valid ? ---> No  due  to  return  statement

2) square =  lambda  (x)  :   x * x
    Is  the  above  lambda  function  valid ? --->  No  due  to  ()  for  argument  'x'

3) Where  does  reference  square  point  to ?  ---> Lambda   function

4) How  is  lambda  function  called ?  ---> Through  refernce  square
																   i.e.  square(5)

5) square = lambda  x :  x * x
    How  to  replace  the  above  lambda  function  with  a  regular  function ?  --->  def   square(x):
											                              															  return  x *  x
'''

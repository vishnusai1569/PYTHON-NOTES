# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) #   'a'  is  100 ,  'b'  is  200 , 'c'  is  default  value  10 , 'd'  is  default  value  20 , result  is  330
print(add(100 , 200 , 300)) # 'a'  is  100 ,  'b'  is  200 , 'c'  is  300 , 'd'  is  default  value  20 , result  is  620
print(add(100 , 200 , 300 , 400)) # 'a'  is  100 ,  'b'  is  200 , 'c'  is 300 , 'd'  400 , result  is  1000
print(add(b = 100 , a = 200))  # 'a'  is  200 ,  'b'  is  100 , 'c'  is  default  value  30 , 'd'  is  default  value  20 , result  is  330
print(add(100 , 200 , d = 300)) # 'a'  is  100 ,  'b'  is  200 , 'c'  is  default  value  10 , 'd'  is 300 , result  is  610
print(add(d = 100 , a = 200 , b = 300)) # 'a'  is  200 ,  'b'  is  300 , 'c'  is  default  value  10 , 'd'  is  100, result  is  610
#print(add(c = 100 , d = 200 , 300 , 400)) # error  due  to  pa  after  ka
#print(add(100 , 200 , c = 300 , x = 400)) # error  becoz arg  'x'  does  not  exist  for add()  function
#print(add()) # error  beoz  args  are  not  passed  for  'a'  and  'b'

#  Gift
# Find  outputs
x = 5
adder1 = lambda    y  :  x + y
x = 10
adder2 = lambda    y  :  x + y
x = 20
adder3 = lambda    y  :  x + y
print(adder1(100))  #   'y'  is  100   result  is  20 + 100 = 120
x = 30
print(adder2(200))   #   'y'  is  200   result  is  30 + 200 =  230
x = 40
print(adder3(300))   #   'y'  is  300   result  is  40 + 300 =  340


'''
Value  of  'x'  at  the  time  of  function  call  matters  but  not  value  of  'x'  at  the  time  of  function  definition
'''

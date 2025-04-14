# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) #  'y'  is   100 , 'x'  is  default  value  5  and  result  is   105
print(adder2(200))  #  'y'  is   200 , 'x'  is  default  value   10  and  result  is   210
print(adder1(300 , 400)) #  'y'  is   300 , 'x'  is   400   and  result  is    700

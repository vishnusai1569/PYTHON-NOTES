# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))  #  Nested  tuple
print(list(a))  # Converts   nested  tuple  to  list  of   tuples  i.e.  [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}  #  set  of  tuples
print(list(b))   # Converts   set  of    tuples  to  list  of   tuples  i.e.  [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})  #  Nested  sequence
print(list(c))     # Converts   nested  sequence  to  list  of  sequence  i.e.  [[10 , 20] , (30 , 40) , {50,60}]

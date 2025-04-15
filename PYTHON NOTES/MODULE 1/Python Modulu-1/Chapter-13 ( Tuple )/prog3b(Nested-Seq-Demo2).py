# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70  # Error becoz  tuple  is  immutable
print(a) #  [10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a)  #  [10, [80, 90], 50, 60]

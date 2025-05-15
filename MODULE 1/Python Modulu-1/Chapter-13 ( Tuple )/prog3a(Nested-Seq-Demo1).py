# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)  #  (10, [70, 30, 40], 50, 60)
#a[1] = [80 , 90 , 100] #  Error  becoz  tuple  is immutabe
print(a)  #  (10, [70, 30, 40], 50, 60)


'''
1) Can  outer  sequence  be  modified ?   --->  No  becoz  it  is  a  tuple

2) Can  inner  sequence  be  modified ?   --->  Yes  becoz  it  is  a  list
'''

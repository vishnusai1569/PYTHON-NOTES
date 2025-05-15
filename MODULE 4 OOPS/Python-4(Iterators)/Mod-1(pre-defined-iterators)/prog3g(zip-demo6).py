# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25)) #   Creates  an  empty  zip  object
a = [ [x , y]  for  x , y   in   z]  #   Creates  a  list  with  elements  of  each  tuple  yielded  by   zip  iterator
print(a)  #  [[0 , 20] , [1 , 21] , [2 , 22] , [3 , 23] , [4 , 24]]



'''
1) What  is  the  result  of  range(5)  --->  0   1    2    3    4

2) What  is   the  result  of  range(20 , 25)  --->  20    21    22    23    24

3)   x      y         [x , y]          a
   ----------------------------------------------
      0      20        [0 , 20]       [[0 , 20]]
      1      21         [1 , 21]        [[0 , 20] , [1 , 21]]
      2      22         [2 , 22]      [[0 , 20] , [1 , 21] , [2 , 22]]
      3      23         [3 , 23]      [[0 , 20] , [1 , 21] , [2 , 22] , [3 , 23]]
      4      24         [4 , 24]      [[0 , 20] , [1 , 21] , [2 , 22] , [3 , 23] , [4 , 24]]
'''
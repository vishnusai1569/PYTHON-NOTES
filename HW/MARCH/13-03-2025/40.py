'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
c=[]
for i in a:
    for j in i:
        c.append(j)
print(c)

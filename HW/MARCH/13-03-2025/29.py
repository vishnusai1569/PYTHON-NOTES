'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''

k=int(input("enter no of rows:"))
m=int(input("rnter no of coloums:"))
for i in range(k+1):
    l=[[0]*m]*i
print(l)
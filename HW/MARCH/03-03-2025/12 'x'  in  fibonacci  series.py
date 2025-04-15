'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? ---> Found

3) Do  not  generate  fibonacci  series
'''



k=int(input('enter the number x :'))
a=0
b=1
c=a+b
mylist=[0,1]
for i in range(100):
    c=a+b
    a=b
    b=c
    mylist.append(c)
if k in mylist:
    print('found')
else:
    print("not found")




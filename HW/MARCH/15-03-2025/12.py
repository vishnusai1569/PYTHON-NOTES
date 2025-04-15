a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35#error
print(a)
print(id(a))
c=list(a)
c[2]=35
#How  to  modify  30  in  tuple  to  35
print(tuple(c))
print(id(c))
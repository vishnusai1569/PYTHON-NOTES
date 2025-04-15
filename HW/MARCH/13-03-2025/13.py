'''
Gift
Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list
'''
a = eval(input("Enter list"))
b = set(a)  # 10 20 15 18 19
ctr = 0
for i in range(len(a)):  # 0 1 2 3 4
    if a.count(a[i]) > ctr:  # 4>0
        ctr = a.count(a[i])  # 4
        mode = a[i]  # 10
print(mode)

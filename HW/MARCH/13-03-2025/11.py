'''
Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  --->
    How  many  elements  are  in  the  list ?  --->  4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  ---> All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? ---> 3

3) Hint: Use  len()  and  count()
'''
a=list(map(eval,input("enter the list:").split()))

if len(a)== a.count(a[0]):
    print("All  the  elements  are  identical")
print(len(a))
print(a.count(a[0]))
print(a)


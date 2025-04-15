'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15 is  found  at  index  2
                 15 is  found  at  index  5
                 15 is  found  at  index  8
                 15 is  found   3  times
'''

a=[10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
k=int(input("enter the number to be searched :"))#15
count=0
if k not  in a:
    print("not found")

else:
    for i in range(len(a)):
        if k==a[i]:
            print(k,'is found at index',i)
            count+=1
            continue
    print(k,"is found",count,"times")
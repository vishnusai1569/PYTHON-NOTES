'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? ---> 2 * i   where 'i'  varies  from   1  to  20
'''


n=int(input("enter the number :"))
sum=0
i=1
while i<=n:
    sum=sum+2*i
    i = i + 1
print(sum)
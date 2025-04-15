'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n
'''

n=int(input("enter the number :"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i = i + 1
print(sum)
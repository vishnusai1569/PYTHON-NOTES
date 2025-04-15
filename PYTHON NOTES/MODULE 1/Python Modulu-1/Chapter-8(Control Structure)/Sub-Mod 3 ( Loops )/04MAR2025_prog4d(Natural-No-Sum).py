'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n
'''
n = int(input('How  many  terms  would  you  like  to  add   :  '))
sum = 0
for   i   in   range(1 , n + 1):
			sum +=  i
print('Sum :  ' ,  sum)

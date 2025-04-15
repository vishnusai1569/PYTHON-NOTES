'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + 2 * 1 - 1 + 2 * 2 - 1 + 2 * 3 - 1 +  ... + 2 * 20 - 1

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20
'''
sum = 0
for  i  in  range(1 , 21):
	sum +=  2 * i - 1
print('Sum  of  first  20  odd  numbers :  ' , sum)

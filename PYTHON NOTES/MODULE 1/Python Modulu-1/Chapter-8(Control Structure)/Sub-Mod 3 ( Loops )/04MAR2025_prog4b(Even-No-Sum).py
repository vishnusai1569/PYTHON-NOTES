'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? ---> 2 * i   where 'i'  varies  from   1  to  20
'''
sum = 0
for  i  in  range(1 , 21):
	sum +=  2 * i;
print('Sum  of  first  20  even  numbers :  ' , sum)

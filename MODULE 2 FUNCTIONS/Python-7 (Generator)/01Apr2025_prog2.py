'''
Write  a   program  to  print  roman  equivalent  of  a  number
1000 -  M , 900  -  CM , 500 -  D , 400 - CD , 100 -   C , 90  -  XC , 50  -  L , 40  -  XL , 10  -  X ,
9  -  IX , 5  -  V , 4  -  IV , 1  -  I

1) Let  input  be  3878,
    What  is  the  output ? ---> MMMDCCCLXXVIII

2) What  is  the  result  of  3878 // 1000 ?  ---> 3
     How  many  M's  are  concatenated  to  string ?  --->  'MMM'
     What  is  the  result  of  3878 % 1000 ?  --->  878

3) What  is  the  result  of  878 // 900 ?  ---> 0
     How  many  CM's  are  concatenated  to  string ?  --->  Nothing
     What  is  the  result  of  878 % 900 ?  ---> 878

4) What  is  the  result  of  878 // 500 ?  ---> 1
     How  many  D's  are  concatenated  to  the  string ?  --->  'D'
     What  is  the  result  of  878 % 500 ?  ---> 378
      and  so  on
'''
def  roman(n):
	a = [1000 , 900 , 500 , 400 , 100 , 90, 50 , 40 , 10 , 9 , 5 , 4 , 1]
	b = ['M' , 'CM'  , 'D' , 'CD'  , 'C' , 'XC' , 'L' , 'XL' , 'X' , 'IX'  , 'V' , 'IV' , 'I']
	c = ''
	for  i   in  range(13):  #  i = 2
		count = n // a[i]  # x = 878 //  500 =  1
		c += b[i] * count #  c = '' + 'M' * 3 = 'MMM' + 'CM' * 0 + 'D' * 1
		n %= a[i]  # n = 878 %  500 = 378
	return c
n = int(input('Enter any number :  '))  #  3878
print('Roman  Equivalent :   ' , roman(n))


# Repeat  the  same  program  with  dictionary
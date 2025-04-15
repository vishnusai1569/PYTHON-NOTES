'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  ---> ADKPZ13579

1) Hint:  sorted()  function , isalpha() , isdigit()  and   join()  method

2)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

3) alpha = ''
    digit = ''

4) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''
a = input('Enter  string  with  alphabets  and  digits  :  ')
b = sorted(a)
alpha = digit = ''
for  ch   in   b:
	if  ch . isalpha():
		alpha  += ch
	elif  ch . isdigit():
		digit  += ch
# End  of  for  loop
print('Result  :  ' ,  alpha + digit)

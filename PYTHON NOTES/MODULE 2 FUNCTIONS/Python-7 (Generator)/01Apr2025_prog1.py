'''
Write  a  program  to  print  each  digit  of  the  number  in  words

Let  input  be  9247
What  is  the  output  ?  ---> Nine  Two  Four  Seven
'''
def  words(a):
	b = ['Zero' , 'One' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine']
#           0           1           2            3           4          5          6          7            8            9
	c = ''
	for  ch  in  a:
		c += b[int(ch)] + ' '  #  c  =  '' + 'Nine' + ' ' + 'Two' + ' ' + 'Four'+  ' '  + 'Seven' +  ' '
	return  c
a = input('Enter any  number  :  ')  #  9247
print('Each  digit  in  words :  ' , words(a))


'''
Repeat  the  above  program  using  dictionary
d = {0 : 'Zero' , 1 : 'One' , 2 : 'Two' , ..... , 9 : 'Nine'}
'''
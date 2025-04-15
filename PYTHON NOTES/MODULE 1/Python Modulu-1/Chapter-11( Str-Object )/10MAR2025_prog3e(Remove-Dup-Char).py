'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
    What  is  the  output ? --->  RAM<space>O

2) out = '' + 'R' + 'A' + 'M' + ' ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
																						Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->  Ignore  the  character

5) Hint:  Use  not  in   operator
'''
a = input('Enter  any  string  :  ')
b = ''
for  ch  in   a:
	if   ch   not  in   b:
		b  += ch
print('String  without  duplicates  :   ' , b)


'''
Input  ---->  RAMA RAO
b   ---> ''
          ch          ch  not  in   b                                   b
    -----------------------------------------------------------------------------------------
          'R'         'R'  not  in  ''  =  True             b = '' + 'R' = 'R'
          'A'         'A'  not  in  'R'  =  True          b = 'R' + 'A' = 'RA'
          'M'         'M'  not  in  'RA'  =  True       b = 'RA' + 'M' = 'RAM'
          'A'         'A'  not  in  'RAM'  =  False    b = 'RAM'
          ' '          ' '  not  in  'RAM'  =  True       b = 'RAM' + ' ' = 'RAM '
          'R'          'R'  not  in  'RAM '  =  False   b = 'RAM '
          'A'          'A'  not  in  'RAM '  =  False   b = 'RAM '
          'O'          'O'  not  in  'RAM '  =  True    b = 'RAM ' + 'O' = 'RAM O'
'''

'''
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

2) What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'

3) i        b[-i]           c
   ---------------------------------------------
                              ''
    1         'city'       '' + 'city' + ' ' =  'city '
    2         'green'    'city ' + 'green' + ' ' =  'city green '
    3         'is'           'city green ' + 'is' + ' ' = 'city green is '
    4         'Hyd'       'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '
   --------------------------------------------------------
'''
a = input('Enter  any  sententce : ')
b = a . split()
c = ''
for  i  in   range(1 , len(b) + 1):
	c += b[-i] + ' '
print('Reverse  order  of  words : ' , c)



'''
Let  input  be  'Hyd is green city'
1) What  is  object  'a'  ?  --->  Hyd is green city

2) What  is  list  b ?  --->   ['Hyd' , 'is' , 'green' , 'city']

3) What  is   object  'c'  ?  --->  city green is Hyd
'''

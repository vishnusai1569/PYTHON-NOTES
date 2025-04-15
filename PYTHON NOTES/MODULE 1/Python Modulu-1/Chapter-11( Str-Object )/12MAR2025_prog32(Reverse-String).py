'''
Write  a  program  to  reverse  a  string  without  slice

1) Let  input  be   Hyd
    What  is  the  output ?  ---> dyH

2)   H       y      d
      -3     -2     -1

      i       a[-i]            b
    ---------------------------------------
                                ''
     1         'd'            '' + 'd' = 'd'
     2         'y'            'd' + 'y' = 'dy'
     3         'H'            'dy' + 'H' = 'dyH'
  ---------------------------------------------
'''
a = input('Enter  any  string : ')  #   HYD
b = ''
for   i   in  range(1 , len(a) + 1):
	b += a[-i]
print('Reverse  String :  ' ,  b)

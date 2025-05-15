'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
1) chr(65) =  'A'
    chr(90) = 'Z'
    chr(97) =  'a'
    chr(122) = 'z'

2) What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character

3) ord('A') =  65
    ord('Z') = 90
    ord('a') =  97
    ord('z') =  122

4) What  does  ord()  function  do ?  --->  Converts  character  to  unicode  value

5) Hint:  Use  two  for  loops
'''
ch = 'A'
while  ch <= 'Z':
	print(ch , end = '  ')
	ch = chr(ord(ch) + 1)
print()
ch = 'a'
while  ch <= 'z':
	print(ch , end = '  ')
	ch = chr(ord(ch) + 1)
print()

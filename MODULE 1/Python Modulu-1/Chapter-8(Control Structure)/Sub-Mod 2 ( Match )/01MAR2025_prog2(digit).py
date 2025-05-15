'''  (Home  work)
Write  a  program  to  print  digit in  words
0  -   Zero
1  -   One
2  -   Two
...
9  - Nine
10 -  Not  a  digit

Hint:  Use  match  ..  case
'''
digit = int(input('Enter   any  digit(0 - 9)  :  '))
match  digit:
	case  0:
			print('Zero')
	case  1:
			print('One')
	case  2:
			print('Two')
	case  3:
			print('Three')
	case  4:
			print('Four')
	case  5:
			print('Five')
	case  6:
			print('Six')
	case  7:
			print('Seven')
	case  8:
			print('Eight')
	case  9:
			print('Nine')
	case  _:
			print('Not  a  digit')

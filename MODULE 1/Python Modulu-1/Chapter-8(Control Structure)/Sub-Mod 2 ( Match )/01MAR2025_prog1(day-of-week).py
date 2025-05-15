'''  (Home  work)
Write  a   program  to  print  day  of  the  week
1  - Monday
2  - Tuesday
3  - Wednesday
....
7 - Sunday
8 - Invalid

Hint:  Use  match ... case
'''
day = int(input('Enter  any   digit (1 to  7) :   '))
match  day:
	case  1:
		print('Monday')
	case  2:
		print('Tuesday')
	case  3:
		print('Wednesday')
	case  4:
		print('Thursday')
	case  5:
		print('Friday')
	case  6:
		print('Saturday')
	case  7:
		print('Sunday')
	case  _:
		print('Invalid  Input')

'''
What  are   the  outputs  if  input  is  1 ?  ---> Invalid  index

What  are   the  outputs  if  input  is  2 ?  ---> Invalid  index

What  are   the  outputs  if  input  is  3 ?  ---> No  result

What  are   the  outputs  if  input  is  4 ?  ---> Invalid  argument (or)  operand

What  are   the  outputs  if  input  is  5 ?  ---> Object  does  not  exist

What  are   the  outputs  if  input  is  6 ?  ---> Div by 0 is not allowed

What  are   the  outputs  if  input  is  7 ?  ---> Invalid  argument (or)  operand

What  are   the  outputs  if  input  is  8 ?  ---> Invalid dict key
'''
ch = eval(input('Enter  choice (9-exit) : '))
while  ch  <  9:
	try:
		match  ch:
			case  1:
				list = [10 , 20 , 15 , 12 , 18]
				print(list[5]) # IndexError  becoz  5  is  invalid  index  for  list
			case  2:
				s = 'Hyd'
				print(s[3]) # IndexError  becoz  3  is  invalid  index  for  'Hyd'
			case  3:
				print(int('Two')) # ValueError  becoz  there  is  no  result
			case  4:
				a = 25
				print(len(a)) # TypeError  becoz  25  is  invalid  arg  for   len()  function
			case  5:
				print(eval('Hyd')) # NameError  becoz  object  Hyd  does  not  exist
			case  6:
				print(7 / 0) # ZeroDivisionError
			case  7:
				print(10 + '20') # TypeError  becoz  10  and   '20'   are  invalid  operads  for  '+'
			case   _:
				d = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb'}
				print(d[18]) #  KeyError  becoz   18  is   invalid dict key
	except   ZeroDivisionError:
		print('Div by 0 is not allowed')
	except  ValueError:
		print('No  result')
	except  IndexError:
		print('Invalid  index')
	except  TypeError:
		print('Invalid   argument (or)  operand')
	except  KeyError:
		print('Invalid dict key')
	except  NameError:
		print('Object  does  not  exist')
	except:
		print('A new error')
	ch = eval(input('Enter  choice(9 - Exit) : '))
# End of while loop
print('Bye')
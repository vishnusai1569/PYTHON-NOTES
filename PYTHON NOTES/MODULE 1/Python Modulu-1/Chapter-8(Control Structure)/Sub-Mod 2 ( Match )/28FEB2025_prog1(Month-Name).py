# Write  a  program  to  print  month  name  for  input  month  number  with  match ... case
try:
	m = eval(input('Enter  month  number (1 - 12) :  '))  #    7.0
	match   m:
		case  1:
			print('January')
		case  2:
			print('February')
		case  3:
			print('March')
		case  4:
			print('April')
		case  5:
			print('May')
		case  6:
			print('June')
		case  7:
			print('July')
		case  8:
			print('August')
		case  9:
			print('September')
		case  10:
			print('October')
		case  11:
			print('November')
		case  12:
			print('December')
		case  _:
			print('Invalid  month  number')
	# End  of  match
	print('Bye')
except:
	print('Input  should  be  an  integer')



'''
What  is   _   called ?  --->  Anonymous  object  (or)  Nameless  object
'''

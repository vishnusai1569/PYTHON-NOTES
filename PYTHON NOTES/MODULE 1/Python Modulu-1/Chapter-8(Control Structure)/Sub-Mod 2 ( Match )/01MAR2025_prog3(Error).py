# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:  #  Error becoz it  is  in  the  middle  of  match
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:   #  Error becoz  it   is  in  the  middle  of  match
		print('Hello')
	case  _: #  Valid
		print('Bye')
print('End')


'''
How  many  times  can  case  _  be  used  in  match ?  --->  One  or  none  but  not  more  than  one
'''

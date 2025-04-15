'''
(Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
try:
	index = a . rindex('city')
	while  index != -1:
		print(index)
		index = a . rindex("s",0 , index-1)
	print('End')
except ValueError:
	pass
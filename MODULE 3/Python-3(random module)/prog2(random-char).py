# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
import random
try:
	a = input('Enter any string : ')
	for x in range(10):
		print(random.choice(a))
except:
	print('Enter atleast one character')
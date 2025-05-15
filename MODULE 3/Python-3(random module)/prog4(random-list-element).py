# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
import random
try:
	a = eval(input('Enter a List : '))
	for x in range(10):
		print(random.choice(a))
except:
	print('Enter atleast one element')
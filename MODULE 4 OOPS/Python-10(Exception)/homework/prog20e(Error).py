# Identify  error   (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else1')
else: # ERROR:  Only one else suite  is permitted for each try suite
	print('else2')
finally:
	print('finally')
print('end')


'''
1) How  many  except  suites  are  permitted  for  a  try  suite  ?   --->  Multiple

2) How  many  else  suites  are  permitetd  for  a  try  suite ?   --->   One  (or)  none

3) How  many  finally  suites  are  permitted  for  a  try  suite ?   --->  One  (or)  none
'''
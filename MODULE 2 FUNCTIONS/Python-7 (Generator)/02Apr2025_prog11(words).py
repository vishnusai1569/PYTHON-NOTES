'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
import time
def   f1(s):
	list = s . split()
	for  word  in  list:
		yield   word
# End of generator
s = input('Enter  any   string  :  ')
g = f1(s)
print('Words  of  the  string')
for  x  in   g:
	print(x)
	time . sleep(1)

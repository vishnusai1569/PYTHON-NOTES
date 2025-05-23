'''
Write  a  function  to  search  for  a  word  in  the  file  and   return  number  of  times  it  is  found

Let  file  contain
Hyd  is  green  city.
Hyd  is  hitec  city.
Hyd  is  beautiful  city.

What  is  the  result  when  'Hyd'  is  searched  in  the  file ?  --->  3
'''
def   search(f ,  word):
	s = f . read() #  Reads  whole  text  of  the  file  into  a  str  object  's'
	return  s . count(word)  #  Number  of times  'word'  is  in  str object  's'
#End of  the  function
try:
	fname = input('Enter filename : ')  #  Reads  filename
	f = open(fname, 'r')  #  Opens  file  in  read  mode
	word = input('Enter  the  word  to  be  searched : ')  #  Reads  the  word
	print(F'{word}  is  found  {search(f , word)}  times')
	f . close() #  Closes  the  file
except:
	print('File  does  not  exist')
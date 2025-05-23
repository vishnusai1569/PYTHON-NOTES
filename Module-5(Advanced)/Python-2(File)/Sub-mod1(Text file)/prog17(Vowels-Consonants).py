'''
Write   a  program  to  count  number  of   lines , characters , words , vowels , consonants ,  spaces , tabs  and   sentences  in  a  file

Let  file  contain

Rama Rao
9247<tab>Sita
+-$ Hyd
                           0		 1             2            3              4             5                  6             7
List  'a'  --->   [  3       27            6            2              1             0                  6             8]
                      Lines    Chars     Words   Spaces     Tabs     Sentences    Vowels     Consonants

Hint:  Use  count()  method  of  Str  class
'''
def  count(f):
	s = f . read()   #  Reads  whole  text  of  the  file  to  str  object  's'
	list = []  #   Empty  list
	list . append(s . count('\n')) #  Appends  number  of  lines  in  the  file  to  list
	list . append(len(s))  #  Appends  number  of  characters  in  the  file  to  list
	a = s . split()  #  Splits  str  object  on  white  space
	list . append(len(a))  #  Appends  number  of  wrods  in  the  file  to  list
	list . append(s.count(' ')) #  Appends  number  of  spaces in  the  file  to  list
	list . append(s.count('\t'))   #  Appends  number  of  tabs  in  the  file  to  list
	list . append(s.count('.'))  #  Appends  number  of  sentences  in  the  file  to  list
	vowel = 'aeiouAEIOU'
	v = c = 0
	for  ch  in  s:  #   ch   is  each  char  of  the  string
		if  ch  in  v:   #  Is  ch  vowel
			v += 1  #  Counts  number  of vowels
		elif  x . isalpha():   # ch  is  alphabet  but  not  vowel  implies  consonant
			c += 1  #  Counts  number  of  consonants
	list . append(v)  #  Appends  number  of  vowels  in  the  file  to  list
	list . append(c)  #  Appends  number  of  consonants  in  the  file  to  list
	return  list   #   Returns  list
#  End  of   function
try:
	fname = input('Enter filename : ')  #  Reads  filename
	f = open(fname , 'r')  #  Opens  file  in  read  mode
	a = count(f) #   Returns  a  list  of  8  elements
	f . close() #  Closes  the  file
	b = ['Lines' , 'Chars' , 'Words' , 'Spaces' , 'Tabs' , 'Sentences' , 'Vowels' , 'Consonants']
	for  i  in  range(8):
			print(b[i] , a[i] , sep = '...')  #  Prints each  msg   in  list  'b'  and  result  in  list  'a'
except:
	print('File  does  not  exist')
'''
Write  a  program  to  print  contents  of  the  file

 File ------------>  str  obj    -------------> monitor
            read()                           print()
'''
def  disp(f):
	s = f . read()   #  Reads  the  whole  file into  a  str  object  's'
	print(F'Contents of  {f . name}')
	print(s)  #  Writes  the  whole  text  in  object  's'  to  the  file
# End  of  the  function
try:
	fname = input('Enter  filename :  ')  #  Reads  the  filename
	f = open(fname , 'r')   # Opens  the  file  in  read  mode
	disp(f)   #  Prints  the  file
	f . close() # Closes  the  file
except:
	print(F'File  {fname}  does  not  exist')



'''
1) Let  file  contain
    Rama  Rao
    9247
    +-$
    Hyd is green city
    s = f . read()
    What  does  object  's'  contain ?  --->  'Rama Rao\n9247\n+-$\nHyd is green city\n'

2) s = f . read()
    print(s)
    How  to  reduce  the  two  statements  to  a  single  statement ?  ---> print(f . read())
'''
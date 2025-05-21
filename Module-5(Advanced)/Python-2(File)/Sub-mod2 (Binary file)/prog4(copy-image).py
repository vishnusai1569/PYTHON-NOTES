# Write  a  program  to  copy  photograph (or) image  present  in  a  binary  file  to  another  file
def   copy(f1 , f2):
	obj = f1 . read() #   Reads  the  image  present  in  1st  file  to  object
	f2 . write(obj)  # Writes  the  obj  to  2nd  file
	print('Image  is  copied  to  swamiji.jpg')
#  End  of  the  function
try:
	f1 = open('sringeri.jpg' , 'rb')
	f2 = open('swamiji.jpg' , 'wb')
	copy(f1 , f2)
	f1 . close()
	f2 . close()
except FileNotFoundError:
	print('File  sringeri.jpg  does  not  exist')


'''
1) What  does  binary  file  contain ?  --->  Images  and  objects

2) Is  'b'  mandatory  to  open  binary  file ? --->  Yes  and  Error  without  'b'
'''
# Find  outputs (Home  work)
import  re
itr  =  re . finditer('[IEY]' , 'Hyd Is greEn citY', re . IGNORECASE)
while  True:
	try:
		m = next(itr)
		print(m . group() , 'is found at index : ' , m . start())
	except  StopIteration:
		break
'''
y is found at index 1
I is found at index 4
e is found at index 9
E is found at index 10
i is found at index 14
Y is found at index 16


  Iteration    m . group()      m . start()
----------------------------------------------
     1                  'y'                  1
     2                 'I'                  4
	 3                 'e'                  9
	 4                'E'                  10
	 5                'i'                   14
	 6                'Y'                 16



1) What  does  re . finditer('[iey]' , 'Hyd is green city')  do ?  --->
									Searches  for  three  characters  'i' , 'e'  and 'y'  in  the  string  'Hyd is green city'

2) What  does  re . finditer('iey' , 'Hyd is green city')  do ?  --->
						Searches  for  the  string  'iey'  in  the  string  'Hyd is green city'  becoz  there  are  no  []

3) What  does  re . finditer('[iey]Hyd' , 'Hyd is green city')  do ?  --->
						Searches  for  three  strings   'iHyd' , 'eHyd' , 'yHyd'  in  the  string  'Hyd is green city'
'''
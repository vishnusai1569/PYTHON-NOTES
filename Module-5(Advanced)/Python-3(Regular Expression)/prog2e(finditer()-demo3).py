# Find  outputs (Home  work)
import   re
itr  =  re . finditer('[A-Za-z0-9]' , 'm$9 K,d%5@E&')
while  True:
	try:
		m = next(itr)
		print(m . group() , ' is  found  at  index :  ' , m . start())
	except:
		break
'''
m is found at index 0
9 is found at index 2
K is found at index 4
d is found at index 6
5 is found at index 8
E is found at index 10
'''

'''
Iteration     m . group()    m . start()
---------------------------------------------
        1          	  'm'                  0
        2        	  '9'                   2
        3            'K'                   4
        4            'd'                   6
        5            '5'                   8
        6            'E'                   10
'''
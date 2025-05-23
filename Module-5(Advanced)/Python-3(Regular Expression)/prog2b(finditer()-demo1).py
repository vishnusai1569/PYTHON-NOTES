'''  (Home  work)
What  are  the  outputs
if  1st  input  is  'Hyd is green city. Hyd IS hitec city. Hyd Is hiS city'  and
2nd  input  is  'is'  ?  --->  is is found between indexes 4 and 5
                                        IS is found between indexes 23 and 24
							            Is is found between indexes 42 and 43
							            iS is found between indexes 46 and 47
							           Found 4 times
'''
import re
string  =  input('Enter  any  string  :  ')
pattern = input('Enter  pattern  to  be  searched : ')
itr = re . finditer(pattern , string , re . IGNORECASE)
ctr = 0
while  True:
	try:
		m = next(itr)
		print(F'{m . group()}  is found  between   indexes   {m . start()}  and {m . end() - 1}')
		ctr += 1
	except  StopIteration:
		break
print('Found ' , ctr ,' times')




'''
itr = re . finditer('is' , 'Hyd is green city. Hyd IS hitec city. Hyd Is hiS city' , re . IGNORECASE)

    Iteartion	next(itr)           m . group()		m . start()                                              	m . end()
---------------------------------------------------------------------------------------------------------------------
        1      First  Match  object      'is'             First  occurance  of  'is'  i.e. 4                4 + len('is') = 4 + 2 = 6
        2      2nd   Match  object      'IS'           Second  occurance  of  'IS'  i.e. 23         23 + len('Is') = 23 + 2 = 25
	    3      3rd  Match  object       'Is'            Third  occurance  of  'iS'  i.e.  42           42 + len('iS') = 42 + 2 = 44
	    4      4th  Match  object       'iS'             Last  occurance  of  'iS'  i.e. 46             46 + len('IS') = 46 + 2 = 48
'''
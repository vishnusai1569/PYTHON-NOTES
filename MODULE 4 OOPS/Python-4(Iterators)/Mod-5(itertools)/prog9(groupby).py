# groupby  iterator  demo  program
import  time
from  itertools  import  groupby
list = [
		{
			'Name' :  'Rama Rao',
			'City' : 'Hyderabad',
			'State' : 'Telangana'
		},
		{
			'Name' :  'Sita',
			'City' :  'Warangal',
			'State' : 'Telangana'
		},
		{
			'Name' : 'Rajesh',
			'City' : 'Karimnagar',
			'State' : 'Telangana'
		},
		{
			'Name' :  'Rajesh',
			'City'  :  'Vijayawada',
			'State' : 'Andhra Pradesh'
		},
		{
			'Name' :  'Amar',
			'City' :  'Vizag',
			'State' :  'Andhra Pradesh'
		},
		{
			'Name' :  'Kiran',
			'City' :  'Banglore',
			'State' : 'Karnataka'
		},
		{
			'Name' :  'Kishore',
			'City' : 'Mysore',
			'State' : 'Karnataka'
		},
		{
			'Name' : 'Gopal',
			'City' : 'Chennai',
			'State' : 'Tamilnadu'
		},
		{
			'Name' : 'Srinath',
			'City' : 'Chennai',
			'State' : 'Tamilnadu'
		},
		{
			'Name' : 'Purna',
			'City' : 'Coimbatore',
			'State' : 'Tamilnadu'
		},
	] #   List  of  dictionaries
g = groupby(list , lambda  dict : dict['State'])  #  Empty  object
while  True:
	try:
		tpl = next(g)  #  Tuple  of   2  elements
		print('State :  ' ,  tpl[0]) #  Value  of  state
		for  dict  in   tpl[1]:  #   Iterates  the  dictionaries  held  by   tpl[1]
			print(dict)
			time . sleep(1)
		print()
	except:
		break


'''
1) What  are  the  two  arguments  of  groupby()  iterator ?  --->  Sequence  of  dictionaries
																												and
																									    Lambda  function  (or)  regular  dunction

2) Why  are  dictionaries  grouped  based  on  State ?  --->  Since  lambda  function  returns  dict['State']

3) What  is  the  constraint  in  the  list ?  --->  Dictionaries  with  same  state  should  be  consecutive  in  the  list

4) How  to  group  based  on  city ?  --->  lambda  dict :  dict['City']
'''
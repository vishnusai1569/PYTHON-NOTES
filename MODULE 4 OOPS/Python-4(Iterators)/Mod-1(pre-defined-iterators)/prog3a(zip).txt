# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
c = enumerate(a)  #  enumerating  list  'a'
for  index , element  in  c:  #  index  and  elements  are elements  of  each  tuple  yielded    by  enumerator
	print(F'{element:15}  ... {b[index]}')
	time . sleep(1)

'''
Telangana...Hyderabad
Andhra  Pradesh...Amaravathi
Karnataka...Bangalore
TamilNadu...Chennai
Maharastra...Mumbai
'''


'''
Iteration      index        element                   b[index]
-------------------------------------------------------------------
     1                0           'Telangana'            'Hyderabad'
     2                1           'Andhra Pradesh'   'Amaravathi'
     3                2           'Karnataka'            'Bangalore'
     4                3           'TamilNadu'           'Chennai'
     5                4           'Maharastra'         'Mumbai'
-------------------------------------------------------------------
What  does  :15  do ?  --->  Prints  string  in  a  width  of  15  characters  with  trialing  spaces
'''
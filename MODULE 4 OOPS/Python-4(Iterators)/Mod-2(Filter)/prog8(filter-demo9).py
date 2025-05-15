# Find  outputs (Home  work)
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(3)
		except:
			break
a = [   { 'country' : 'India' , 'sale' : 150.5} ,
          { 'country' : 'china' , 'sale' : 200.2} ,
          { 'country' : 'USA' , 'sale' : 300.3} ,
          { 'country' : 'UK' , 'sale' : 210.4} ] #   List  of  dictionaries
f1 = filter (lambda  x  :   x['country'] . startswith('U') , a) #  Creates  an  empty  filter  object
print('Filter  f1')
disp(f1)  # Those  dictionaries  where   value  of   country  name  starts  with  'U'
f2 = filter(lambda  x  :  x['sale']  >=  200  , a) # creates another empty filter object
print('Filter  f2')
disp(f2)  # Those  dictionaries  where   value  of  sale  is  >= 200


'''
Filter  f1
{ 'country' : 'USA' , 'sale' : 300.3}
{ 'country' : 'UK' , 'sale' : 210.4}
Filter  f2
{ 'country' : 'china' , 'sale' : 200.2}
{ 'country' : 'USA' , 'sale' : 300.3}
{ 'country' : 'UK' , 'sale' : 210.4}
'''



'''
1) What  is  'x' ?  --->  Each  dictionary  of  list  'a'

2) What  is  x['country'] ?  --->  Value  of  country  in  dictionary  'x'

3) What  is  x['sale'] ?  ---> Value  of  sale  in  dictionary  'x'
'''
#  replace()  method  demo  program
a = 'Hyd  is  green  city.  Hyd  is  hitec  city.  Hyd  is  his  city'
b = a . replace('is' , 'was')
print(b) #  Hyd  was  green  city.  Hyd  was  hitec  city.  Hyd  was  hwas  city
print(a)  #  Hyd  is  green  city.  Hyd  is  hitec  city.  Hyd  is  his  city'


'''
replace()  method
---------------------
1) What  does  replace(old  string, new string) do ?  --->
													Returns  a  string  where  every  occurance  of  old  string  is  replaced  with  new  string

2) a . replace('is' , 'was')
    Is  object  'a'  modified  after  execution  of  replace()  method ?  --->	No   becoz  str  object  is  immutable

3) a = a . replace('is' , 'was')
     Is  the  above  statement  valid ?  ---> Yes  and  reference  is  modified  but  not  object
     															  i.e.  Ref  'a'  points  to  the  new  string
'''

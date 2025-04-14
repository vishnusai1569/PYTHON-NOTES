# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]  #  List  of  dictionaries
b = sorted(a , key = lambda  x  :  x['Year']) # Sorts the dictionaries in the list according to 'Year' in ascending order
print(b) # [{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,{'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} , {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ]
#print(sorted(a)) # Error :  Key  arg  is  missing


'''
1) What  is  x  ? --->  Each  inner  dictionary   of  list  'a'

2) What  is  x['year']  ?  --->  Value  of  year  in  dict  'x'
											   i.e.  2013 , 1999  and  2008

3) sorted(list  of  tuples)
    What  is  the  default  key ?  ---> First  element  of  each  inner  tuple

4) sorted(list  of  dictionaries)
    What  is  the  default  key ?  ---> None  and  sorted()  function  throws  error

5) In  other  words,  key  argument  is  mandatory  when  it  is  list  of  dictionaries
'''

# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) # {15 : 'Sita' , 17 : 'Kiran' }
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # {10 : 'Rama' , 18 : 'Rajesh' , 12 : 'Rama Rao'}



'''
1) What  does  a . items()  return ?  --->  dict_items([(10 , 'Rama') , (15 , 'Sita') , (18 , 'Rajesh') , (17 , 'Kiran') , (12 , 'Rama Rao')] )

2) Iteration   k       v              k % 2 != 0      dict  'b'
    -----------------------------------------------------------------------
            1			10      'Rama'       False             { }
            2			15 	  'Sita'         True              {15 : 'Sita'}
            3			18      'Rajesh'     False             {15 : 'Sita'}
            4			17      'Kiran'        True             {15 : 'Sita' , 17 : 'Kiran'}
            5			12      'Rama  Rao'    False        {15 : 'Sita' , 17 : 'Kiran'}

3) Iteration   k    a[k]     a[k] . startswith('R')      dict  'c'
   --------------------------------------------------------------------------------------------
            1		10     'Rama'           True                    {10 : 'Rama'}
            2		15     'Sita'             False                   {10 : 'Rama'}
            3		18     'Rajesh'        True                    {10 : 'Rama' , 18 : 'Rajesh'}
            4		17     'Kiran'           False                   {10 : 'Rama' , 18 : 'Rajesh'}
            5		12     'Rama  Rao'   True                    {10 : 'Rama' , 18 : 'Rajesh' , 12 : 'Rama Rao'}
'''

#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
del   a['Sal'] #How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao' }



'''
1) How  to  remove  key : value  pair  of  dictionary  ?  --->  del  dict[key]

2) What  does  del  dict[Invalid  key]  do ? --->  Throws  Error

3) a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
    Is  del  a['Married']  valid ?  --->  No  becoz  there  is  no  key  married  in  dictionary  'a'

4) How  to  delete  the  whole  dictionary ?  --->  del   dict
'''

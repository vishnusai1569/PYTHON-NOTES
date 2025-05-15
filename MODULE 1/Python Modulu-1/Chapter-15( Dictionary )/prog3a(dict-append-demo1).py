#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender'] = 'M'   #How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married'] = True   #How  to  append  'Married' :  True  to  dictionary  'a'
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65   ,  'Gender' : 'M' , 'Married' :  True }



'''
1) dict[valid-key] = value
    What  does  the  above  statement  do ?  --->  Modifies  value  of  the  key  in  the  dictionary

2) dict[invalid-key] = value
    What  does  the  above  statement  do ?  --->  Appends  new  key : value  pair  to  the  dictionary
'''

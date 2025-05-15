# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a)) # address of the dictionary
a['Sal'] =  2000  #  How  to  modify  1000.65  to  2000
a['Ename'] = 'Sita' #How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno'] = 35 #How  to  modify  25   to  35
print(a) # {'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  :  2000}
print(id(a)) # Same  address



'''
1) Can  key  be  modified  ?  --->  No

2) Can  value  be  modified ?  --->  Yes  with  dict[key] =  value
'''

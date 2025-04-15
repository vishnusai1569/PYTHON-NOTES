# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'} #  Dictionary
print(a) #  {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))  #  <class  'dict'>
print(a[10]) #   Value  of  10  i.e.  Ramesh
print(a[20])  #   Value  of  20  i.e.  Kiran
print(a[15])  #   Value  of  15  i.e.  Amar
print(a[18])  #   Value  of  18  i.e.  Sita
#print(a[19])   #  Error  becoz  19  is  not  a  valid  key
#print(a[0])    #  Error  becoz  0  is  not  a  valid  key
#print(a['Amar'])    #  Error  becoz  'Amar'  is  not  a  valid  key
a[15] = 'Krishna'  # Modifies  value  of  15  to  'Krishna'
del   a[20]  #    Removes  20 : 'Kiran'  from  dict  'a'
a[25] = 'Vamsi'  #  Appends  25 : 'Vamsi'  to  dict  'a'
print(a)  #  {10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita' , 25 : 'Vamsi'}
print(len(a))  # 4
#print(a * 2)  # Error  becoz  dict  can  not  be  repeated

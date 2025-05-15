# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')  #   prints  Sec  and  Cyb  and  None is   returned
print(type(a))  #<class 'tuple'>
print(a)  #(type and address of  lambda function , None ,None)
for  x  in  a:
	print(x) # type and address of  lambda function <next line>None<nextline>None
#a() #Error :  tuple  can  not  called  as  it  is  not  a   function
print(a[0]())  #(lambda  :  print('Hyd'))() ---> Hyd <next line>None

'''
Sec
Cyb
<class  'tuple'>
(type and address of  lambda function , None ,None)
type and address of  lambda function
None
None
Hyd
None
'''

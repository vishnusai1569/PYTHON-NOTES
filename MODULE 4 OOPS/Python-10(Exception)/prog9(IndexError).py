
# Which  of  the  following  statements  throw  IndexError ?  (Home  work)
print('Hyd'[0])  #  H
print('Hyd'[1]) #   y
print('Hyd'[2])  #  d
#print('Hyd'[3]) # IndexError  :   Index  3  does not  exist  in   'Hyd'
list = [10 , 20 , 15 , 18]
print(list[0]) #   10
print(list[3])#   18
#print(list[4]) # IndexError :  Index  4  does not  exist  in  the  list
print(list[-1])  #   18
print(list[-4]) #  10
#print(list[-5]) # IndexError :  Index  -5  does not  exist  in   the  list
tpl = (10 , 20 , 30)
#print(tpl[3]) # IndexError  :  Index  3  does not  exist  in  tuple
r = range(10)
#print(r[10]) # IndexError :  Index  10  does not  exist  in   range(10)
s = {10 , 20 , 15 , 18}
#print(s[4])   #  TypeError  :   Invalid  operand  4  for  set   's'  as  set  is  not  indexed
d = {10 : 'Hyd' , 20 : 'Sec'}
#print(d[0])  #  KeyError  :  0  is  invalid  key  for  dict  'd'


'''
When  is  IndexError  raised  ?  --->   When  the  index  is  out  of  range  i.e.  invalid  index
'''
'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''

k=input("enter the string:")
if len(k)<=4:
    print("")
else:
    p=k[0:2]
    x=k[-2::1]
    print(p+x)
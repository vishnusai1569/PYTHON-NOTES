# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5) #  lam = lambda  x :  3 * x ** 2 + 4 * x + 5  --->  Ref  lam  points  to  lambda  function
print(lam(2)) #3* 2** 2 + 4*2 + 5 = 3*4 + 4*2 + 5 = 25
print(lam(2.5)) #3* 2.5** 2 + 4*2.5 + 5 = 3*6.25 + 10 + 5 = 33.75
print(lam(4)) #3* 4** 2 + 4*4 + 5 = 3*16 + 16 + 5 = 48 + 21 = 69
print(lam) #   Type  and  address  of  lambda  function
#print(lam()) #  Error :  Arg  is  not  passed  for  'x'


'''
1) Regular  function  returns  lambda  function  which  is  assigned  to  object  lam

2) lam(2)  executes  lambda  function
'''

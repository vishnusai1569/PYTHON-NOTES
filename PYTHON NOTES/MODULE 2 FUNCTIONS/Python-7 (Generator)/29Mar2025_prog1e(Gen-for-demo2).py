# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()  #  1st  generator  object
print(next(g))  #  1st  element  of   1st  gen  object  i.e.  25
for  x  in   g:   #  'x'  is  each  element  of  1st  gen  object  'g'  from  2nd  element
	print(x)    #  10.8  <next line>   Hyd  <next line>
print()
for  x  in   f1():  #  'x'  is  each  element  of  2nd   gen  object  'g'  from  1st   element
	print(x)   #  25  <next line>   10.8  <next line>  Hyd  <next line>
print()
gen = f1()    #  3rd  gen   object
print(next(gen))  #  1st  element  of  3rd  gen  object  i.e.  25
for  x  in   f1():   #  'x'  is  each  element  of  4th   gen  object  'g'  from  1st   element
	print(x)     #  25  <next line>   10.8  <next line>  Hyd  <next line>
print(next(gen))  #  2nd  element  of  3rd  gen  object  i.e.  10.8

'''
25
10.8
Hyd
25
10.8
Hyd
25
25
10.8
Hyd
10.8
'''

'''
1) How  many  generator  objects  are  in  the  above  program ?  --->  4

2) When  is  generator  object  created ?   --->  As  soon  as  f1()   is  encountered
'''

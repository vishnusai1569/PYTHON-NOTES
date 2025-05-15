# Modify  following  program  with  regular  function  and  for  loop  (Home  work)
import  time
def  even(x):
	return   x % 2 == 0
a = [25 , 9 , 10 , 15 ,  17 , 24 , 35 , 47 , 0 , 19 , 53 , 18 , 65 , 83]
f = filter(even  , a)
print(type(f))
print(f)
for   y   in   f:
	print(y) #   10  <next  line>  24  <next  line>  0   <next  line>  18  <next  line>
	time . sleep(1)

'''
1) for  y  in  filter(even  , a):
			print(y)
    When  is  even()  function  executed ?  --->	For  each  element  of  list  'a'

2) def  even(x):
	     pass
    f = filter(even , a)
    What  is  the  value  of  argument  'x'  for  even()  function ? ---> Each  element  of  list  'a'

3) What  happens  when  even()  function  returns  False ?  --->  Ignores  'x'  and  moves  to  next  element  of  list  'a'

4) What  happens  when  even()  function  returns  True ?  --->   'x'  is  returned  to  for  loop  variable  'y'
'''
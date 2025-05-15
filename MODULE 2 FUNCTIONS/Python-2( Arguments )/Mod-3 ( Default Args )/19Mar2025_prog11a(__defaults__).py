#  __defaults__   demo  program
def  f1(a , b , c = 25 , d = 'Hyd' , e = [10 , 20 , 30] , f = (40 , 50 , 60)):
        pass
def   f2(x , y , z):
	pass
def   f3(x , y , z = 10.8):
	pass
#End of the function
print(f1 . __defaults__)  #  (25 , 'Hyd' , [10,20,30] , (40,50,60))
print(type(f1 . __defaults__)) #  <class  'tuple'>
print(f2 . __defaults__)  #  None  but  not  ()
print(type(f2 . __defaults__)) #  <class  'NoneType'>
print(f3 . __defaults__)  # (10.8,)



'''
__defaults__
-----------------
1) What  is    __defaults__  ?  --->  A  tuple  with  all  the  default  values  of  arguments  of  the  function

2) What  is  the  syntax  of  __defaults__ ?  ---> functionname . __defaults__

3) What  is   f1 . __defaults__ ?  --->  A  tuple  consisting  of  default  values  of  arguments  of  f1  function

4) Who  is  initializing   __defaults__ ?  ---> PVM

5) When  is   __defaults__  initialized ?  ---> As  soon  as  function  is  defined

6) What  is  the  value  of  __defaults__ when  there  are  no  default  arguments ?  --->  None  but  not  empty  tuple

7) If  a  function  modifies   values  of   default  arguments,  __defaults__  is  automatically  modified
    becoz  they  point  to  same  object
'''

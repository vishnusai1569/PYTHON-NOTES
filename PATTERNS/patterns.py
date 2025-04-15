'''
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)#{10 , 20}
print(c)#{10 , 20}
print(type(c))#class set
d = a - b
print(d)#{10 , 20}
print(type(d))#class set
print(c  is  d)#False
print(c  ==  d)#True
#----------------------------
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)#{10,20,50,60}
print(type(c))#class set
d = a ^ b
print(d)#{10,20,50,60}
print(type(d))#class set
print(c   is   d)#False
print(c  ==   d)#True
#----------------------------
a = {x * x  for   x   in   range(10)}
print(a)#{0,1,4,9.16,25,36,49,64,81}
print(type(a))#class set
#--------------------------------
x=eval(input("Enter List:"))#[False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
print(list(set(x)))
#------------------------------------
x=eval(input("Enter 1st List:"))
y=eval(input("Enter 2nd List:"))
a=set(x)
b=set(y)
c= list(a & b)
print(c)
#--------------------------------------------'

a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a. get('Empno'))
print(a. get('Ename'))
print(a. get('Sal'))
#-------------------------------'

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
print(id(a))
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35
print(a)
print(id(a))
#-------------------------------------'

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a.update({'Gender' : 'M'})#How  to  append  'Gender' : 'M'  to  dictionary  'a'
a.update({'Married' : True})#How  to  append  'Married' :  True  to  dictionary  'a'
print(a)
#---------------------------------------------------------------------------------------

# Find  outputs (Home  work)
a = { }
b= {10 : 'Rama',20 : 'Sita',15 : 'Rajesh',18 : 'Kiran'}
a.update(b)
#How  to  append  10 : 'Rama'  to  dictionary  'a'
#How  to  append  20 : 'Sita'  to  dictionary  'a'
#How  to  append  15 : 'Rajesh'  to  dictionary  'a'
#How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a)
#------------------------------------

#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.popitem()
#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)
#--------------------------------------------------------'

def p(s):

    return s == s[::-1]

# Get input from the user
a= input("Enter a string: ")

# Check if the input string is a palindrome
if p(a):
    print("palindrome")
else:
    print("not a palindrome")
#==========================================

#1)
#  return  statement  demo  program
def  f1():
	print('f1  function')#2)f1 function
	return  25
	print('Hello')
# End  of  the  function
print('Begin')#1)Begin
x =  f1()
print(x)#3)25
print('End')#4)End
#===========================================

# Find outputs  (Home  work)
def   f1():
	print('Hyd')#Hyd
	print('Sec')#Sec
	print('Cyb')#Cyb
# End  of  the  function
print('Begin')#Begin
x = f1()
print(x)
print(type(x))#None type
print('End')#End
#==================================================

#  Gift
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)#(10,20,30)
print(type(x))#class tuple
a , b , c =  f1()
print(a)#10
print(b)#20
print(c)#30
print('for  loop')
for  k   in  f1():
      print(k)
#======================================'

# Find  outputs
def    f1():
        return  10#10
        return  20
        return  30
# End  of  the  function
print('Begin')#Begin
x = f1()
print(x)
print('End')#End
#return 100
#============================================='

f1()
def   f1():
        print('Hello')
print(f1())
print(f1) #error
#=============================================

# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
#================================================='

# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)
#f1(40 ,50)
#f1(60)
#f1()
#============================================================

def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(60)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(40,50)
def  f1(x , y , z):
	print('Three  argument  function :',x,y,z)
f1(10 , 20 , 30)
#============================================================'

# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)#correct results
disp('Sita',20000.0, 35)#incorrect results
#===========================================================

# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')#a:Cyb <tab> b:'Sec' <tab> c:'Hyd'
f1(c = 3 + 4j , a = True , b = None)#a:True <tab> b: None <tab> c = 3 + 4j
f1(25 , c = 10.8 , b = 'Hyd')#a:25 b:'Hyd' c:10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function'
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c''
#================================================================
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x,y,z)'
#==================================================
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))
print(f1(*[6 , 7 , 8]))
#print(f1([6 , 7 , 8]))
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))
#print({{'c' : 2 , 'b' :  4 , 'a' : 6}})
#print(f1({'c' : 2 , 'a' :4,'x':6}))'
#================================================'

# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))#error
print(sorted(a , rev = True))#error
print(25 , 10.8 , 'Hyd' , separator = '\t') #error
print(25 , 10.8 , 'Hyd' , endofline = '\t')#error
print(25 ,  sep = '\t' ,10.8 , end='\t','Hyd')#error'
#==========================================================='

def prime(n):
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
#End of the for loop
        return True
n = int(input('Enter any number:'))
if n<2:
    print('Invalid input')
elif prime(n):
    print('Prime number')
else:
    print('Composite number')

#19/3/25
# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)#a : 10    b : 20
f1(b = 30 , a = 40)#a : 30    b : 40
#f1(50 , 60)#error
#f1(70 , b = 80)#error
#==============================================='

#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)#a : 10   b : 20   c : 30
f1(a = 40 , b = 50 , c = 60)#a : 40   b : 50   c : 60
f1(c = 100 , b = 90 , a = 80)#a : 80   b : 90   c : 100
#f1(70 , 80 , c = 90)#error
#f1(70 , 80 , 90)#error
#f1(c =15,b=25,35)#error
#===========================================================

# Identify error (Home  work)
def   f1(a  , b , *):#*should comes before formal parametres
     pass #Indensation error
#===============================================================

#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)
f1(40 , 50 , c = 60)
f1(a = 70 , b = 80 , c = 90)
f1(a = 100 , b = 110 , 120)
f1(a = 130 , 140 , c = 150)
f1(160 , b = 170 , 180)
f1(190 , b = 200 , c = 210)f1(10 , 20)#a:10 b:20
#f1(a = 30 ,  b = 40)#error
#f1(50 , b = 60)#error
#f1(a=70,80)#error due to pa after ka
#===========================================================

# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)#a:10 b:20 c:30
f1(40 , 50 , c = 60)#a:40 b:50 c:60
#f1(a = 70 , b = 80 , c = 90)#error
#f1(a = 100 , b = 110 , 120)#error
#f1(a = 130 , 140 , c = 150)#error
#f1(160 , b = 170 , 180)#error
#f1(190 , b =200,c=210)#error
#=========================================='

# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)#a:10 b:20 c:30 d:40 e:50 f:60
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)#error
#f1(1 , 2 , 3 , 4 , 5 , f = 6)#error
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)#error
f1(10 , 20 , 30 , 40 , e=50,f=60)#a:10 b:20 c:30 d:40 e:50 f:60
#=============================================

def  f1(/ , a , b ,  c):#error atleast one variable should before slash
        pass
def   f2(a , b , c , *):#error atleast one variable should after star
        pass
#==============================================='

def  f4(* , a , b , c , /):
	        pass #confusion of abc are ka or pa
#=================================================

def  f1(x):
	print('1st  function : ' , x) #error
def  f1(y):
	print('2nd  function : ' , y)#error
def  f1(z):
	print('3rd  function : ' , z)#3rd function:10
f1(z = 10)
#f1(y = 20)
#f1(x = 30)
#===========================================================

# Identify  Error
#def   f1(a = 10 ,  b ,  c = 20 ,  d):#error ka follows pa
	pass
def   f2(b , d , a = 10 ,c=20):
	pass#Indesation error
#=========================================================='

#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)#10
# End  of  the  function
f1(20) #20
f1()
#f1(a = 30)
#========================================================
# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))#330
print(add(100 , 200 , 300))#620
print(add(100 , 200 , 300 , 400))#1000
print(add(b = 100 , a = 200))#330
print(add(100 , 200 , d = 300))#610
print(add(d = 100 , a = 200 , b = 300))#610
#print(add(c = 100 , d = 200 , 300 , 400))#error ka follows pa
#print(add(100 , 200 , c = 300 , x = 400))#error
#print(add())#error
#==================================================================
#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))
print(f1())
print(f2(20))
#print(f2())# error due to missing 1 required positional argument: 'x'
#====================================================================

# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)#------
disp('$')#$$$$
disp()#****
disp(n = 5)#*****
disp(5)#20
disp(n = 7 , ch = '%')#%%%%%%%
disp(7 , '@')#@@@@@@@
disp(7 , n = 6)#42
#disp(ch='!',5)#error due to ka after pa'
#============================================================='

# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))#64
print(power(5))#25
print(power(b = 3 , a = 4.5))#91.125
print(power(3 + 4j))#(-7+24j)
print(power(True))#1
#def   power(b = 2 , a): #error
#	 pass#error
#==========================================================='

# Find outputs  (Home  work)
def   add(a , b):
	print('2-argument  function')
	return a + b
def  add(a , b , c):
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function')#4-argument  function
	return a + b  + c + d
# End  of  the  function
# last function will be called
print(add(10 , 20 , 30 , 40))#100
print(add(50 , 60 , 70))#184
print(add(80 , 90))#177
print(add(100))#109
print(add())#10
#==============================================================

# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)#3-argument  function  :10,20,30
disp(40 , 50 , 60 , 70)#error
disp(80,90)#3-argument  function  :80,90,25
#======================================================

# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))#70
print(add())#30
print(add(a = 50))#70
print(add(b = 60 , a = 70))#130
#print(add(80,90))#error
#=======================================================

# Find  outputs(Home  work)
#def   add(a = 10 , b , c):#error
 #       pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))#120
print(add(b = 60 , c = 70))#140
print(add(c = 80 , b = 90 , a = 100))#270
#print(add(c = 25 , a = 43))#error
#print(add(1 , 2 , 3))#error
#def   add(a , b = 10 , c ,  * , d  , e =20,f):#error
#		pass
#==============================================================

# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1._defaults_) # error double underscore is missing for defaults
#==================================================================
def   f1(a = []):
        pass
print(f1.__defaults__)#([],)
#=================================================================

# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__)
f1(3)#[3]
print('__defaults__  :  ' , f1.__defaults__)#([3],)
f1(4 , [1 , 2 , 3])#[1 , 2 , 3, 4]
print('__defaults__  :  ' , f1.__defaults__)#([3],)
f1(9)#[3,9]
print('__defaults__  :  ' , f1.__defaults__)#([3,9],)
f1(40 , [10 , 20 , 30])#[10,20.30,40]
print('__defaults__  :  ' , f1.__defaults__)#([3,9],)
f1(5)#[3,9,5]
print('__defaults__  :  ' , f1.__defaults__)#([3,9,5],)
f1([6 , 7 , 8])#[3,9,5,[6,7,8]
print('__defaults__  :  ' , f1.__defaults__)#([3,9,5,[6,7,8]],)
#==================================================================

#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__)
f1(3)#[3]
print('__defaults__  :  ' , f1.__defaults__)#([],)
f1(4 , [1 , 2 , 3])#[1,2,3,4]
print('__defaults__  :  ' , f1.__defaults__)#([],)
f1(4)#[4]
print('__defaults__  :  ' , f1.__defaults__)#(([],)
f1(40 , [10 , 20 , 30])#[10,20,30,40]
print('__defaults__  :  ' , f1.__defaults__)#(([],)
f1(5)#[5]
print('__defaults__  :  ' , f1.__defaults__)#([],)
f1([6 , 7 , 8])#[6,7,8]
print('__defaults__  :  ' , f1.__defaults__)#([],)
#=============================================================='

# Find  outputs(Home  work)
def     f1(x , a = []):#(x,4)
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('__defaults__  :  ' , f1.__defaults__)#([],)
print(f1(3))#[0,1,4]
print('__defaults__  :  ' , f1.__defaults__)#([0,1,4],)
print(f1(4 , [10 , 20 , 15 , 18])) #[10 , 20 , 15 , 18 , 0 , 1 ,4 ,9]
print('__defaults__  :  ' , f1.__defaults__)#([0,1,4],)
print(f1(5))#[0,1,4,0,1,4,9,16]
print('__defaults__  :  ' , f1.__defaults__)#([0,1,4,0,1,4,9,16],)
print(f1(a = [100 , 200 , 300],   x = 6 ))#[100 , 200 , 300,0,1,4,9,16,25]
print('__defaults__  :  ' , f1.__defaults__)#([0,1,4,0,1,4,9,16],)
print(f1(6))#[0,1,4,0,1,4,9,16,0,1,4,9,16,25]
print('__defaults__  :  ' , f1.__defaults__)#([0,1,4,0,1,4,9,16,0,1,4,9,16,25],)
#============================================================================================

# Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3))#[0,1,4]
print(f1(4 , [10 , 20 , 15 , 18]))#[10 , 20 , 15 , 18,0,1,4,9]
print(f1(5))#[0,1,4,9,16]
print(f1(a = [100 , 200 , 300],   x = 6))#[100,200,300,0,1,4,9,16,25]
print(f1(6))#[0,1,4,9,16,25]
#============================================================================================='

# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__)#('Hyd',[])
f1()#a: HydSec b:[1,2,3]
print('Default Values  :  ' , f1 . __defaults__)#('Hyd',[1,2,3])
f1()#a: HydSec b:[1,2,3,1,2,3]
print('Default Values  :  ' , f1 . __defaults__)#('Hyd',[1,2,3,1,2,3])
f1()#a: HydSec b:[1,2,3,1,2,3,1,2,3]'
#==========================================================================================

# Right-Angled Triangle
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()'
    
#========================================
# Pyramid Pattern
n = 5
for i in range(1, n+1):
    print(" " * (n-i), end="")  # Space before stars
    print("*" * (2*i - 1))  # Odd number of stars
    
#=====================================================
# Inverted Pyramid Pattern
n = 5
for i in range(n, 0, -1):
    print(" " * (n-i), end="")  # Space before stars
    print("*" * (2*i - 1))  # Odd number of 
   
#=====================================================
# Hollow Square Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
#=======================================================
# Diamond Pattern
n = 5

# Upper part of diamond
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i - 1))

# Lower part of diamond
for i in range(n-1, 0, -1):
    print(" " * (n-i), end="")
    print("*" * (2*i - 1))
    
#==============================================================
n = 5
for i in range(1, n+1):
    print('*' * i)
#================
n = 5
for i in range(n, 0, -1):
    print('*' * i)'
    
#======================================================
# n = 5
# for i in range(1, n + 1):
#     print(' ' * (n - i), end="")
#     print( ''.join(str(x) for x in range(1, i + 1)), end="")
#     print(''.join(str(x) for x in range(i - 1, 0, -1)))

n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + ''.join(str(x) for x in range(1, i + 1)) + ''.join(str(x) for x in range(i - 1, 0, -1))
#===================================================================================== 
n = 5
for i in range(1, n+1):
    print('*' * i)
    #Right angle triangle

#================================
n = 5
for i in range(n,0, -1):
    print('*' * i)
    #Reverse Right angle triangle
    #==========================
    
n = 4
for i in range(n):
    print('*' * n)
    #square
    
    #=============================
n = 5
for i in range(1, n+1):
    print(' ' *(n-i), end="")
    print('*' *(2*i-1))
    #pyramid
    
#=====================================
n = 5
for i in range(n,0,-1):
    print(' ' *(n-i), end="")
    print('*' *(2*i-1))
    #Reverse pyramid
    
    #==============================
n = 5
for i in range(1, n+1):
    print(' ' *(n-i), end="")
    print('*' *(2*i-1))
for i in range(n-1,0,-1):
        print(' ' *(n-i), end="")
        print('*' *(2*i-1))
        #Diamond
        
#====================================
last=71
for i in range(7):#0---->6
    str=''
    for j in range(65,last+1):#65,71+1-->65,72
        str+=chr(j)#---->chr(65) to chr(71)
    print(str, end='')
    print(' '*(2*i-1),end='')
    
    if i == 0:
        revstr=str[::-1]#GFEDCBA
        print(revstr[1:])#FEDCBA
    else:
        print(str[::-1])
    last-=1
'''
    #===============================================

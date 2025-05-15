'''
Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

1) Let  object  'a'   contain   2 / 3  and   object  'b'  contain  5 / 9
    What  is  the  result  of  a > b ?  --->  True  due  to 18 > 15
    What  is  the  result  of  a < b ?  --->  False  due  to  18  is  not  <  15
    What  is  the  result  of  a == b ?  --->  False  due  to  18  is  not  =  15
    What  is  the  result  of  a >= b ?  ---> True  due  to 18 >= 15
    What  is  the  result  of  a <= b ?  --->  False  due  to  18  is  not  <=  15
    What  is  the  result  of  a != b ?  --->  True  due  to 18 != 15

2) Imp  point  is  cross  product

3) What  is  the  method  call  to  __gt__()  method ?  --->  a > b
     What  is  the  method  call  to  __lt__()  method ?  --->  a < b
     What  is  the  method  call  to  __eq__()  method ?  ---> a == b
     What  is  the  method  call  to  __ge__()  method ?  --->  a >= b
     What  is  the  method  call  to  __le__()  method ?  ---> a <= b
     What  is  the  method  call  to  __ne__()  method ?  ---> a != b
'''
class  Rat:
	def  get(self):
			 self . nr = int(input('Enter  numerator  :  '))  #  How  to  read  numerator  and  denominator  into  object  self
			 self . dr = int(input('Enter  denominator  :  '))
	def __gt__(a , b):
			return  a . nr * b . dr >  a . dr * b . nr  #  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def __lt__(a , b):
			return  a . nr * b . dr  <  a . dr * b . nr  #  true  when  rational  number  in  object self  <  that  of  'b'  and  false  otherwise
	def __eq__(a , b):
			return  a . nr * b . dr  ==  a . dr * b . nr  #  true  when  rational  numbers  are  same   and  false  otherwise
	def __ge__(a , b):
			return  a . nr * b . dr >=  a . dr * b . nr  #  return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def __le__(a , b):
			return  a . nr * b . dr <=  a . dr * b . nr   # return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def __ne__(a , b):
			return  a . nr * b . dr !=  a . dr * b . nr   # return  true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
a = Rat()  # How  to  create  two  Rat   class  objects  'a'  and  'b'
b = Rat()
a . get()  #  How  to  read  1st  rational   number  into  object  'a'
b . get()  #  How  to  read  2nd  rational   number  into  object  'b'
if  a > b:   #  __gt__()  method  of   Rat  class  returns  True  when  1st  rational  number  in  object  'a'  is  >  that  of  'b'  and  False  otherwise
	print('>')
if  a < b:  #  __lt__()  method  of   Rat  class  returns  True  when  1st  rational  number  in  object  'a'  is   <  that  of  'b'  and  False  otherwise
	print('<')
if  a == b:  #  __eq__()  method  of   Rat  class  returns  True  when   rational  numbers   in  objects  'a'   and  'b'  are  same  and  False  otherwise
	print('==')
if  a >= b:   #  __ge__()  method  of   Rat  class  returns  True  when  1st  rational  number  in  object  'a'  is   >=  that  of  'b'  and  False  otherwise
	print('>=')
if  a <=  b:   #  __le__()  method  of   Rat  class  returns  True  when  1st  rational  number  in  object  'a'  is   <=  that  of  'b'  and  False  otherwise
	print('<=')
if  a != b:   #  __ne__()  method  of   Rat  class  returns  True  when   rational  numbers  in  objects  'a'   and  'b'  are  not  same   and  False  otherwise
	print('!=')


'''
1) How  many  if  conditions  will  be  True  ?  --->  Any  3

2) What  are  the  outputs  of  the  program  when  object  'a'  contains  2  and  3  and   'b'  contains  5  and  9 ?  --->  > , >=  and  !=

3) What  are  the  outputs  of  the  program  when  object  'a'  contains  2  and  3  and   'b'  contains  5  and  7 ?  --->  < , <=  and  !=


4) What  are  the  outputs  of  the  program  when  object  'a'  contains  2  and  3  and  'b'  also  contains  2  and  3 ?  --->  == ,  >= , <=

5) How  to  call  methods  in  another  way ? --->  a . __gt__(b) , a . __lt__(b) , a . __eq__(b)  and  so  on

6) class  c1:
	      def   __gt__(a , b):
			    print(10 > 20)
			    print(a > b)
    Is  10 > 20  recursion ?  --->  No  becoz  10  and  20  are  integers  but  not  c1  class  objects
    Is  a > b  recursion ?  --->  Yes  becoz  a  and  b  are   c1  class  objects
'''
# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)  #  Object  is  initialized  with  dd = 15 , mm = 8 , yy = 1947 by  constructor
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)  #  Object  is  initialized  with  dd = 26 , mm = 1 , yy = 1950 by  constructor
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)   #  Object  is  initialized  with  dd = 19 , mm = 7 , yy = 1985 by  constructor
print('a  :  ' , a . __dict__)  #  a : {'dd' : 15 , 'mm' : 8 , 'yy' : 1947}
print('b  :  ' , b . __dict__)  #  b : {'dd' : 26 , 'mm' : 1 , 'yy' : 1950}
print('c  :  ' , c . __dict__)  #  c : {'dd' : 19 , 'mm' : 7 , 'yy' : 1985}
#d = Date()  #  Error :  Args  are  not  passed   for  dd1 , mm1 , yy1   of  constructor
#e = Date(dd = 30 , mm = 4 , yy = 2022)  #  Error : There  are no  args  dd , mm , yy  for  constructor
#f = Date(dd1 = 26 , mm1 = 8 , 2023)  #  Error :  PA  2023  after  KA  mm1 = 8



'''
1) a = Date(15 , 8 , 194)
    What  are  15 , 8  and  1947  called ?  --->  Actual  parameters
    What  are  dd1 , mm1  and  yy1  called ?  ---> Formal  parameters
    What  are  dd , mm  and  yy  called ?  --->  Instance  variables

2) What  happens  internally  when  constructor  is  executed  ? --->
																Actual  Parameters  are  copied  to  formal  Parameters
																which  are  further  copied  to  instance  variables
'''
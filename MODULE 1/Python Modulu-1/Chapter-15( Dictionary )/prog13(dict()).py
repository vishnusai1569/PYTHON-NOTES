#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #   List of tuples
b = dict(a) # converts  list  of  tuples  to dict
print(b) # {10 : 'Hyd' , 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])  #  Tuple  oflists
d = dict(c) # converts  tuple  of  lists  to dict
print(d) # {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]] #Nested  list
#print(dict(e)) # error  due  to  more  than  2  elements  in  inner   lists
f = [[10] , [20] , [30]]
#print(dict(f)) # error  due  to  less  than  2  elements  in  inner   lists
#print(dict([10 , 20]))#  Error  becoz  arg  is  not  a  nested  sequence
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) # {10 : [20 ,30]  , 40 : [50,60] , 70 : [80,90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h)) # Error  becoz  key  can  not  be  mutable  object   such  as  list
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) # {(10 , 20) : 30 , (40 , 50) : 60 , (70 , 80) : 90}


'''
dict()  function
------------------
1) What  is  the  argument  of  dict()  function ?  --->
											Nested  sequence  such  as  list  of  tuples , list  of  lists , tuple  of  tuples , tuple  of  lists,
											set  of  tuples  and  so  on

2) What  does  dict(nested-sequence)  do ?  --->  Converts  nested  sequence  to  dictionary

3) How  many  elements  can  be  in  each  inner  sequence ?  --->  Exactly  two  elements
     What  are  the  two  elements  of   each  inner  sequence ?  --->  key  and   value

4) Is  dict(sequence)  valid ?  --->   No  becoz  argument  is  not  a  nested  sequence
'''

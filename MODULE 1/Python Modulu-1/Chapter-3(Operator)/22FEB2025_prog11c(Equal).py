#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a)   #    25
b =  a
print(b)    #  25
print(a  is  b) #   True
x = 4
y = 5
z = x + y * 6
print(z)  #   34
#25 = a  #  Error becoz  25  is  not  a  reference
#a + b = x + y  #  Error becoz  a + b  is  not  a  reference



'''
1) a = 25
    What  does  b = a  do ?  ---> Assigns  reference  'b'  to  the  same  object  where  'a'  points
								                 i.e.  Reference  copy  but  not  object  copy

2) In  other  words  b = a  does  not  copy  value  of  object  'a'  to  object  'b'

3) id  is  copied  but  not  value

4) a = 25
    b = a
    Why  is  25   not  copied  from  object  'a'  to  'b' ?  --->
																		Since  there  can  not  be  multiple  int  objects   with  same  value  25
'''

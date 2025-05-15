# Find   outputs (Home  work)
from  itertools  import  count
c = count()#  1st  count  object
print('While  loop')
while   True:
        x = next(c) #    Yileds  0  to  10  from  1st  count  object
        if   x > 9:
                break
        print(x)  #  But  prints  0  to  9   (does  not  print  10  due  to  break )
print('For  loop')
for  x  in  count():  #    Yileds  0  to   21  from   2nd   count  object
	if  x  >  20:
		break
	print(x)   #  But  prints  0  to   20   (does  not  print   21  due  to  break )
#end  of  for  loop
print('Element :  ' , next(count())) #  Yields  0  from  3rd  count  object  i.e.  0
c = count()  #  4th   count  object
#print(*c)  #  MemoryError becoz   object can  not  hold  0  to  infinity

'''
While loop
0
1
2
3
4
5
6
7
8
9
For loop
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
Element : 0
'''

'''
How  many  count  objects  are  in  the  program  ?  ---> 4
'''
# Find outputs  (Home  work)
import   time
def   disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
	print()
a = [10 , 20 ,  30]
b = {1 : 2 , 3 : 4 , 5 : 6}
c = zip(a , b . keys())  #  Zips  list  'a'   with  the  keys  of   dict  'b'
disp(c)  #  (10 , 1)  <next  line>  (20 , 3)  <next  line>  (30 , 5)  <next  line>
d = zip(a , b . values())   #  Zips  list  'a'  with   the  values  of   dict  'b'
disp(d)  #   (10 , 2)  <next  line>  (20 , 4)  <next  line>  (30 , 6)  <next  line>
e = zip(a , b . items())   #  Zips  list  'a'   with  the   tuples  of  the  list  in  dict_items  object
disp(e)  #  (10 , (1 , 2))  <next  line>  (20 , (3 , 4))  <next  line>   (30 , (5 , 6))  <next  line>
f = zip(a , b)   #  Zips  list  'a'  with  the    keys  of   dict  'b'
disp(f)  #  (10 , 1)  <next  line>  (20 , 3)  <next  line>  (30 , 5)  <next  line>
g = zip(a)   #  Zips  list  'a'
disp(g)   # (10,)   <next  line>  (20,)  <next  line>  (30,)  <next  line>
h = zip(b)   #  Zips  keys  of   dict  'b'
disp(h)  # (1,)   <next  line>  (3,)  <next  line>  (5,)  <next  line>
i = zip()   #  Zips   nothing
disp(i)  #  Nothing



'''
1) What  does  zip(a , b . keys())  do ?  --->  Zips  elements  of  list  'a'  with  keys  of  dict  'b'

2) What  does  zip(a , b . values()) do ? --->  Zips  elements  of  list  'a'  with  values  of  dict  'b'

3) What  does  zip(a , b . items())  do ? --->  Zips  elements  of  list  'a'  with  tuples  of  the  list  in  dict_items  object

4) What  does  zip(a , b)  do ?   --->  Zips  elements  of  list  'a'  with  keys  of  dict  'b'

5) What  does  zip(a)  do ?  ---> Zips  elements  of  list  'a'

6) What  does  zip(b)  do ?  --->  Zips  Keys  of  dict  'b'

7) What  does  zip()  do ?   --->  Zips  nothing
'''
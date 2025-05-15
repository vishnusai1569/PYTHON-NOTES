# Can  dictionary  be  reversed  ? (Home  work)
import   time
def   disp(r):
	while  True:
		try:
			print(next(r))
			time . sleep(1)
		except:
			break
	print()
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Kiran' , 18 : 'Amar'}
b = reversed(a . keys())  #  Creates an  empty  object
disp(b)  #    keys  in  reverse  order  i.e.  18 <next  line>  15   <next  line>   20  <next  line>  10  <next  line>
c = reversed(a . values())  #  Creates another  empty  object  to  iterate  again
disp(c)  #   values  in  reverse  order  i.e.  Amar <next  line>  Kiran   <next  line>  Sita  <next  line>   Rama  <next  line>
d = reversed(a . items())   #  Creates another  empty  object  to  iterate  again
disp(d)  #   Tuples  in  reverse  order  i.e.  (18 ,'Amar')  <next  line>  (15 , 'Kiran')  <next  line> (20 , 'Sita')  <next  line> (10 , 'Rama')  <next  line>
e = reversed(a) #  Creates another  empty  object  to  iterate  again
disp(e)    #    keys  in  reverse  order  i.e.  18 <next  line>  15   <next  line>   20  <next  line>  10  <next  line>


'''
What  is   the  alternative  to  reversed(a . keys()) ?  --->  reversed(a)
'''
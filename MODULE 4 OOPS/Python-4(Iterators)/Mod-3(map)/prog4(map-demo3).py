# Find  outputs (Home  work)
import   time
def  disp(m):
	while   True:
		try:
			print(next(m))
			time . sleep(1)
		except:
			break
list = [    { 'country' : 'India' , 'sale' : 150.5} ,
              { 'country' : 'China' , 'sale' : 200.2} ,
              { 'country' : 'USA' , 'sale' : 300.3} ,
              { 'country' : 'UK' , 'sale' : 210.4} ]  #   List  of  dictionaries
m1 = map(lambda  x  :  x['country'] , list)  #   Creates  an  empty  map  object
print('Map   m1')
disp(m1)   #   India  <next  line>  China  <next  line>   USA  <next  line>   UK  <next  line>
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')
disp(m2)   #   150.5  <next  line>  200.2  <next  line>  300.3 <next  line>  210.4  <next  line>
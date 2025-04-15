#  Gift
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))#23
print(f1(*[6 , 7 , 8]))#62
#print(f1([6 , 7 , 8]))#error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))#16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))#14
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))#error
#print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})#error
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))#error
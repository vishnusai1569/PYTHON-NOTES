#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1() 
#print(len(g)) # Error  becoz  'g'  is  not  a  sequence
#print(g * 3) #  Error becoz  gen  object  can  not be  repeated
#print(g[0]) #    Error becoz  generator  is  not  indexed
#print(g[1 : 3])   #    Error becoz  generator  can  not  be  sliced
print(*g) # 1 <space> 2 <space> 3

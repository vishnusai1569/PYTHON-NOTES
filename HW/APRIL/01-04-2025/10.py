#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
#print(len(g))#no len
#print(g * 3)#unsupported operator
#print(g[0])#error
#print(g[1 : 3])#error
print(*g)

'''1 2 3'''
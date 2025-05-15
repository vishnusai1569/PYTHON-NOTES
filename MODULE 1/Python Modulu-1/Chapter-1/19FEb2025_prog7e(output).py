# Find  outputs
#a = { [ ] : 25} #Error  becoz  list  is  not  an  immutable  object
b = { ( ) : 25} #  Valid
print(b) #  { () : 25}
#c = { { } : 25}   #Error  becoz  dict  is  not  an  immutable  object
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}  #  valid
print(d)  #   {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) #   1
#e = {set() : 10.8}   #Error  becoz  set   is  not  an  immutable  object

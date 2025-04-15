# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))#<class 'function'>
print(type(lamb))#<class 'function'>
print(lamb(2))
print(lamb(5))
print(lamb)#address
#print(lamb())#error
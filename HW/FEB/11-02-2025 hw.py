#1)
a = 3 + 4j
print(a)#3+4j
print(type(a))#<class 'complex'>
print(id(a))#address
print(a . real)#3
print(a . imag)#4
print(type(a . real))#<class 'float'>
print(type(a . imag))#<class 'float'>
print('  ')
#2)
a = 6j
print(a)#6j
print(type(a))#<class 'complex'>
print(a . real)#0
print(a . imag)#6
#print(5 + j6)#error
#print(3 + 4i)#error
#print(4+j)#error
print(4 + 1j)#4+1j
print(4 + 0j)#4+0j
print()

a = True
print(a)#true
print(type(a))#<class 'bool'>
print(id(a))#address
b = False
print(b)#False
print(type(b))#<class 'bool'>
print(True + True)#2
print(True + False)#1
print(False + True)#1
print(False + False)#0
print(True + True + True)#3
print(25 + 10.8 + True)#36.8
print(True > False)#True
print(True)#True
print(False)#False
#print(true)#error
#print(false)#error
print('')


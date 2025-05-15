#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
#b.update(a) # error  due  to  more  than  2 elements in tuple
print(b) # {}
c = [(10,) , (20,) , (30,)]
#b . update(c)  # error  due  to  less  than  2 elements in tuple
print(b) # {}


'''
How  many  can  each  inner  sequence  have ?  --->  2  elements
'''

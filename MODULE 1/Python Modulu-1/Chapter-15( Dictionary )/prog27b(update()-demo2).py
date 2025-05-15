# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b) #{'Y' : 'Yellow', 'G' : 'Green' , 'R' : 'Red'  , 'B' : 'Blue'}
#a . update(b) # error as there is no update method in list

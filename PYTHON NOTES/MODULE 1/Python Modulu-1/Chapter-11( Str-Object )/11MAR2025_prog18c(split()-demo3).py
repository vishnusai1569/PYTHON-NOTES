# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))  # ['Hyd\nis' , 'green\tcity']
print(a . split())  #  ['Hyd' , 'is' , 'green' , 'city']
print(a . split('green'))  #  ['Hyd\nis<space>' , '\tcity']
#print(a . split(''))  #  Error  due  to  empty string  delim

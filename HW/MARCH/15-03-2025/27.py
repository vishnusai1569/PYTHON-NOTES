# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)#{25 , 10.8 , 'Hyd' , True}
print(id(a))#address
a . add(tpl)
a . add('Sec')
print(a)#{True, 'Hyd', 10.8, 'Sec', (10, 20, 30), 25}
print(id(a))#address
print(len(a))#6
#a . add([100 , 200 , 300])#error
#a . add(set())#error
#a . add({ })#error

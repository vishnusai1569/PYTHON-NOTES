# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')  # 10...Hyd <nextline> 20...Sec <nextline> 15...Cyb <nextline> 18...Pune <nextline>
'''
for  x , y   in  a . keys():  # error  due  to  2  variables  x , y
       print(x , y , sep = ' ... ')
for  x , y   in  a . values():  # error  due  to  2  variables  x , y
       print(x , y , sep = ' ... ')
for  x , y   in  a: # error  due  to  2  variables  x , y
       print(x , y , sep = ' ... ')
'''


'''
When  are  two  variables  permitted  in  for  loop ?  --->
																			Only  for  items()  method  but  not  for  keys()  and  values()  methods
'''

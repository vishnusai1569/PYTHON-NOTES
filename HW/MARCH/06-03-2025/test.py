d={1:'1',2:'2',3:'3'}
del d[1]
print(d['1'])
d[1]='10'
del d[2]
print(d)
print(len(d))
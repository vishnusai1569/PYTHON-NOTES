#  Find  outputs (Home  work)
f = open('a.txt' , 'w+')  #  file  handle  is   at  the  begining  of  the  file  soon  after file  is  opened  and  file  is  empty  due  to  w+  mode
print(f . tell()) #  Offset  of  begining  of  the  file  i.e.  0
f . write('Hyd is green city')   #   Writes  string  to  the  file  and  moves  file  handle  to  eof
print(f . tell())  #  Offset  of  end  of  the  file  i.e.  17
f . seek(7) #  Moves  file handle  to that character whose offset is 7 i.e. 8th character
print(f . read(5)) #  Reads  5  characters  from  offset  7   and  moves  file  handle  to  offset  12  i.e. 13th  character
print(f . tell()) #  Offset  of 13th  char  i.e.  12

'''
0
17
green
12
'''
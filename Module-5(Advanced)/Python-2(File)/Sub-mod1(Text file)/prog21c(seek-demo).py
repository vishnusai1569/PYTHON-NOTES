#  Find  outputs  (Home  work)
f = open('a.txt' , 'w+')  #  file  handle  is   at  the  begining  of  the  file  soon  after file  is  opened  and  file  is  empty  due  to  w+  mode
f . write('Hyd is green city.') #   Writes  string  to  the  file  and  moves  file  handle  to  eof
f . seek(0) #  Moves  file  handle  to  the  beginning of  file
f . write('Sec') #  Writes  'Sec'  at  the beginning of the file  replacing  'Hyd'
f . seek(0) #  Moves  file  handle  to  the  beginning of  file
print(f . read()) #  Reads  whole  file  and  moves  file  handle  to  the  end  of  file
f . seek(7) #  Moves  file handle  to that character whose offset is 7 i.e. 8th character
print(f . read(5)) #  Reads  5  characters  from  offset  7   and  moves  file  handle  to  offset  12  i.e. 13th  character
f . seek(0 , 2) #   Moves  file handle  to end of the file
f . write('Hyd is Hitec city.') #  Writes  string  at  the  end  of  file
f . seek(0) #  Moves  file  handle  to  the  beginning of  file
print(f . read()) #  Reads  whole  file  and  moves  file  handle  to  the  end  of  file
f . seek(7) #  Moves  file handle  to that character whose offset is 7 i.e. 8th character
f . write('red') #  Writes  'red'   into  the  file  at   offset  7  replacing  'gre'
f . seek(0) #  Moves  file  handle  to  the  beginning of  file
print(f . read()) #  Reads  whole  file  and  moves  file  handle  to  the  end  of  file

'''
Sec is green city.
green
Sec is green city.Hyd is Hitec city.
Sec is reden city.Hyd is Hitec city.


1)  H   y    d             i     s          g     r     e      e     n            c      i      t      y
     0   1     2     3     4    5    6    7    8     9     10    11    12    13    14    15   16

2) Which  operations  are  permitted  for  w+  ? --->  Read ,  append  and  modify
'''
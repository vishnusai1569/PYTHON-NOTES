

#  dir()  function  demo  program  (Home  work)
from  prog10a   import  rat
a = rat()  #  Empty object
a . nr = 22  #   Adds  variable  nr  to  object  'a'  with  value   22
a . dr = 7  #   Adds  variable  dr  to  object  'a'  with  value   7
print(dir(rat))  #  ['add', 'div', 'get', 'mul', 'simplify', 'sub', 'test' , '__str__' , Environment  variables]
print()
print()
print(dir(a))  #   #  ['add', 'div', 'get', 'mul', 'simplify', 'sub', 'test' , '__str__' , Environment  variables , nr , dr]
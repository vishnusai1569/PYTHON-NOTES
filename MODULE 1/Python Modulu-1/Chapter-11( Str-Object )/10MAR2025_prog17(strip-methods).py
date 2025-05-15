# lstrip() , rstrip()  and  strip()  methods  demo program
a = '       Sankar  Dayal  Sarma         '
print(a . lstrip()) #   Sankar  Dayal  Sarma<spaces>
print(a . rstrip())  #   <space>Sankar  Dayal  Sarma
print(a . strip())  #   Sankar  Dayal  Sarma
print(a)  #      <spaces>Sankar  Dayal  Sarma<spaces>



'''
1) What  does  lstrip()  method  do ?  --->  Returns  a  string  without  leading  spaces

2) What  does  rstrip()  method  do ?  --->  Returns  a  string  without  trailing  spaces

3) What  does  strip()  method  do ?  --->  Returns  a  string  without  leading  and  trialing  spaces

4) a . lstrip()
    a . rstrip()
    a . strip()
    Is  object  'a'  modified  after  execution  of  the  above  three  methods ? --->  No  becoz  str  object  is  immutable
'''

#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)  #  a : 10  <tab>  b : 20
#f1(a = 30 ,  b = 40)  #  Error :  KA's   are not permitted  due  to  /
#f1(50 , b = 60)    #  Error :  KA  b = 60  is   not permitted  due  to  /
#f1(a = 70 , 80)  #  Error :  pa  after  ka

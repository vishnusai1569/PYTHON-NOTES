#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]' ) )  #  Approximate  time  to  store  500  elements  in  the  list
print(timeit('( x * x   for  x  in  range(500) )'  ) )  #  Approximate  time  to  create  an  empty  generator  object

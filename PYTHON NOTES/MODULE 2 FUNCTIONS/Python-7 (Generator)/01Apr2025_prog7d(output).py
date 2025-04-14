# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]   #List  of 10000  elements
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))  #  Empty  geneator  object
print(sys . getsizeof(list)) #  size of list of  10000  elements
print(sys . getsizeof(gen)) #  size of  empty  generator  object

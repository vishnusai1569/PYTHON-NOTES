# Find  outputs   (Home  work)
try:
	print(1)  #   1
	print(7 / 0)  #  Throws  ZDE
	print(3)  #   Skipped  due  to  error i.e.   ZDE
except:
	print(4) #   4
else:   # Skiped  : except  suite  is  already  executed
	print(5)
finally:
	print(6) #   6
print(7) #  7
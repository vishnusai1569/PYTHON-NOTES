
# Find  outputs   (Home  work)
try:
	print(1)  #  1
	print(7 / 0)  #  Throws  ZDE
	print(3) #  Skipped   due  to  error  i.e.   ZDE
except:
	int('Two')  #  Throws  ValueError
else: #  Not executed  :  except  suite  is  already  executed
        print(5)
finally:  #  Executes  finally  suite  becoz  ValueError  is   reported
        print(6)  #  6
print(7)  #  Skipped  becoz  ValueError   is  not   caught


#  ValueError  is  reported  becoz  it  is  not  caught
# Find  outputs   (Home  work)
try:
	print('Outer   try') #  Outer  try
	try:
		print('Inner    try')  # Inner  try
		print(7 / 0) #  Throws  ZeroDivisionError
		int('Hyd')  #  Skipped   due  to  error  i.e. ZDE
		'Hyd'[5]
		eval('Hyd')
	except   ZeroDivisionError:
		print('ZDE   of   inner   try')  #  ZDE   of   inner   try
		int('Ten') #   Executes  finally  suite  before  ValueError is  caught  by  outer  except
	except  ValueError:  #  Skipped :  1st  except  suite  is  already  executed
		print('ValueError  of  inner  try')
	finally:
		print('Inner  try  finally')  #  Inner  try  finally
	print('End  of  inner  try')  #  Skipped  :  ValueError   is  not  yet  caught
except   ValueError:
	print('ValueError  of  outer  try')  #   ValueError  of  outer  try
except   IndexError:
	print('IndexError  of  outer  try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')  #  Outer  try  finally
print('End  of  outer  try')  #  End  of  outer  try
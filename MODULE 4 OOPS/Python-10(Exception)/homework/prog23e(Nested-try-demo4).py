#  Find  outputs (Home  work)
try:
	print('Outer  try') #   Outer  try
	try:
		print('Inner  try')  # Inner  try
		eval('Hyd') #   Executes  finally  suite  befoee  NameError  is  caught  by  outer  except
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally') #  Inner  try  finally
	print('End of inner try')  #  Skipped :  NameError  is  not  yet  caught
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:  #  NameError  is  caught  here
	print('default  except  of  outer  try')  #  default  except  of  outer  try
finally:
	print('Outer  try  finally') #  Outer  try  finally
print('End  of  outer  try')  #  End  of  outer  try
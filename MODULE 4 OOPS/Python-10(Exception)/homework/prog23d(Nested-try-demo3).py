#  Find outputs   (Home  work)
try:
	print('Outer  try')  # 	Outer  try
	try:
		print('Inner  try')   #  Inner  try
		'Hyd'[3] #  finally  suite  is  executed  before   IndexError  is  caught  by  outer  except
		eval('Hyd')  #  Skipped  due  to   error   i.e.   IndexError
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally')  #  Inner  try  finally
	print('End  of  inner  try')   #  Skipped  :  IndexError  is  not  yet  caught
except  ValueError:
	print('ValueError  of  outer  try')
except  IndexError:
	print('IndexError  of  outer  try')  #  IndexError  of  outer  try
except:
	print('default except of outer try')
finally:
	print('Outer try finally')  #  Outer try finally
print('End  of  outer  try') #   End  of  outer  try
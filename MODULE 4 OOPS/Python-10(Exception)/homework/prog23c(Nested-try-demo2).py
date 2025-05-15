#  Find outputs   (Home  work)
try:
	print('Outer  try') #  Outer  try
	try:
		print('Inner  try') #  Inner  try
		int('Hyd') #   Throws  ValueError
		'Hyd'[5]   #  Skipped  due  to  error   i.e.  ValueError
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')    #  ValueError  of  inner  try
	finally:
		print('Inner  try  finally')  #  Inner  try  finally
	print('End  of  inner  try')  #   End  of  inner  try
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default except of outer try')
finally:
	print('Outer try finally') #  Outer try finally
print('End of outer try') #  End of outer try
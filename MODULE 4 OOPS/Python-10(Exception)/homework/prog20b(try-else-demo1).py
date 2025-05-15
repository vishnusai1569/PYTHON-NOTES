# Find  outputs  (Home  work)
try:
	print('try') #   try
	print(7 / 0)  #  Throws  ZDE
except:
	print('except')  #  except
else:   #  Skipped  :  except  suite  is  already  executed
	print('else')
finally:
	print('finally')  # finally
print('End') #   End


'''
1) Are  both  except  and  else  suites  executed ?  --->  No  and  any  one  is  executed  between  else  and  except

2) In  other  words,  else  suite  is  skipped  when  except  suite  is  executed  and  vice-versa
'''
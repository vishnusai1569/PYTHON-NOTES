# Find  outputs  (Home  work)
def   bold(fun): #  fun  is  inner2
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>'  #  return  '<b>'  +  inner2()  +  '</b>'  --->  return  '<b>'  +  '<i><u>Hello  World</u></i>'  +  '</b>'  --->  return  '<b><i><u>Hello  World</u></i></b>'  --->   Returned  to  function  call  inner1()
	return  inner1  #  Returned  to  function  call  bold(inner2)
def   italic(fun): #  fun  is  inner3
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'  #  return  '<i>'  +   inner3() +  '</i>' --->  return  '<i>'  +   '<u>Hello  World</u>' +  '</i>'  --->  return  '<i><u>Hello  World</u></i>'  --->  Returned  to  function  call  inner2()
	return  inner2  #  Returned  to  function  call  italic(inner3))
def   underline(fun): #  fun  is f1
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'  #   return  '<u>'  +  f1()  +  '</u>'  --->  return  '<u>'  +  'Hello  World'  +  '</u>'  --->   return  '<u>Hello  World</u>'  --->  Returned  to  function  call  inner3()
	return  inner3 #  Returned  to  function  call  underline(f1)
@bold  #  Interpreted  as  f1 = bold(italic(underline(f1)))  --->  f1 =  bold(italic(inner3))  --->  f1 = bold(inner2)  --->  f1 = inner1  i.e.  f1  points   to  inner1() function
@italic
@underline
def   f1():
       return  'Hello  World'  #  Returned  to  function  call  f1()
# End  of  the  function
print(f1())  #  print(inner1())  --->  print('<b><i><u>Hello  World</u></i></b>')  --->  <b><i><u>Hello  World</u></i></b>

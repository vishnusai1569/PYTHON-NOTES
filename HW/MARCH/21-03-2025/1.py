# 1. Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)	#[10 , 20 , 15 , 18]
change(a)
print(a)	# [10, 17, 18, 25]


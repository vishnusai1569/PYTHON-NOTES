# Find  output(Home  work)
def  fun():
	x = 10 #  Lv  of   fun()  function
	def    gun():
		#x =  x +  20  #  Error  :  Lv  of  gun()  function  is  not  yet  initialized
		print(x)  #   Lv  of  fun()  function  i.e.  10
	#end of inner function
	gun()
#end of outer function
fun()

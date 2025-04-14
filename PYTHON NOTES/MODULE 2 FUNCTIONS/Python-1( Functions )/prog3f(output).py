#  Find  outputs
#f1() #  Error  : function  call  before  defn
def   f1():
        print('Hello')
print(f1())  #    Hello  <next  line>  None
print(f1)  #  Type  and  address  of  f1  function


'''
1) Can  function  be  called  before  it  is  defined  ?  --->  No

2) In  other  words,  define  the  function  first  and  then  call  the  function

3) print(f1())
    print(f1)
	What  is  the   difference  between  f1()  and   f1 ?  --->  f1()  executes  f1()  function  but
																						   	  print(f1) prints  type  and  address  of  function  f1
'''

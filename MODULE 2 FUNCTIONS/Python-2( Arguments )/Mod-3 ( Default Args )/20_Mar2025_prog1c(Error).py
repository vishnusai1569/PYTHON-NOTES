# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):  # Error due  to  non-default  args  'b' and  'd'  after   default  args  a = 10  and  c = 20
	pass
def   f2(b , d , a = 10 , c = 20):#   Valid :  DA's  after  NDA's
	pass



'''
1) Can  there  be  non-default  arguments  after  default  arguments ?  --->  No

2) What  is  the  order  of  arguments  in  the  function  header ?  --->
																	Non-default  arguments  followed  by  default  arguments

3) In  other  words,  default   arguments  should  be  at  the  end  of  function  header

4) If  an  argument  has  default  value, all  the  remaining  arguments  also  should  have  default  values
'''

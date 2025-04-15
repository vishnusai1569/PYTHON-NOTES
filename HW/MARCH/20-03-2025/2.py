#  Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)
def  avg(*a):
	return sum(a) / len(a) if a else 0
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #15.75
print(avg(25 , 10.8 , True))#12.2666
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))#14.26
print(avg())#0
print(avg(25))#25.0
print(avg(3 + 4j , 5 + 6j))#4+5j
tpl = (10 , 20 , 15 , 18)
#print(avg(tpl))#
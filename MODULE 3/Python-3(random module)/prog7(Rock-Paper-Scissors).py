'''  (Home  work)
Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  --->  Draw

2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  --->  Computer  wins  becoz  parer  dominates  rock

3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  ---> Computer  wins  becoz  scissors  dominates  paper

4) What  is  the  result  computer  selects  rock  and  user  input  is  scissors ?  --->  Computer  wins  becoz  rock  dominates  scissors

5) What  is  the  result  in  all  other  cases  ?  --->  User  wins
'''
from    random    import    choice
list = ['Rock' , 'Paper' , 'Scissors']
while  True:
	ch = int(input('What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  '))
	if  ch  <  0  or  ch  >  2:
		print('Invalid  Input')
	else:
		user = list[ch]
		comp = choice(list)
		print('User  :  ' ,  user)
		print('Computer  :  ' , comp)
		if  user  ==  comp:
			print('Draw')
		elif  (comp  ==  'Paper'  and  user  ==  'Rock')   or  (comp  ==  'Rock'  and  user  ==  'Scissors')   or  (comp  ==  'Scissors'  and  user  ==  'Paper'):
			print('Computer  wins')
		else:
			print('User  wins')
		option = input('Continue  (  y / n)  ?  ')
		if  option  ==  'n'  or  option  ==  'N':
			break
# End  of  while  loop
print('End  of  the  game')
# permutations  and  combinations  iterators
import  time
def  disp(itr):
	while  True:
		try:
			print(next(itr))  #  ('A' , 'B')
			time . sleep(1)
		except:
			break
from  itertools  import  combinations,permutations
list = ['A' , 'B' , 'C' , 'D']
c = combinations(list , 2) #   Empty  object
print('Different  Combinations')
disp(c)  #
print('Different   Permutations')
p = permutations(list , 2)
disp(p)


'''
Different  Combinations
('A', 'B')
('A', 'C')
('A', 'D')
('B', 'C')
('B', 'D')
('C', 'D')
Different   Permutations
('A', 'B')
('A', 'C')
('A', 'D')
('B', 'A')
('B', 'C')
('B', 'D')
('C', 'A')
('C', 'B')
('C', 'D')
('D', 'A')
('D', 'B')
('D', 'C')
'''

'''
What  is  the  second  argument  of  combinations()  and  permutations() ?  --->  Number  of  elements  in  each   tuple
'''
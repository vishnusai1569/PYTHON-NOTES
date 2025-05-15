#  Find  outputs (Home  work)
import  time
def  disp(itr):
	while  True:
		try:
			print(next(itr))
			time . sleep(1)
		except:
			break
from  itertools  import  combinations,permutations
list = ['A' , 'B' , 'C' , 'D']
c = combinations(list , 3)
print('Different  Combinations')
disp(c)
print('Different   Permutations')
p = permutations(list , 3)
disp(p)


'''
Different  Combinations
('A' , 'B' , 'C')
('A' , 'B' , 'D')
('A' , 'C' , 'D')
('B' , 'C' , 'D')
Different   Permutations
('A' , 'B' , 'C')
('A' , 'B' , 'D')
('A' , 'C' , 'B')
('A' , 'C' , 'D')
('A' , 'D' , 'B')
('A' , 'D' , 'C')
('B' , 'A' , 'C')
('B' , 'A' , 'D')
('B' , 'C' , 'A')
('B' , 'C' , 'D')
('B' , 'D' , 'A')
('B' , 'D' , 'C')
('C' , 'A' , 'B')
('C' , 'A' , 'D')
('C' , 'B' , 'A')
('C' , 'B' , 'D')
('C' , 'D' , 'A')
('C' , 'D' , 'B')
('D' , 'A' , 'B')
('D' , 'A' , 'C')
('D' , 'B' , 'A')
('D' , 'B' , 'C')
('D' , 'C' , 'A')
('D' , 'C' , 'B')
'''
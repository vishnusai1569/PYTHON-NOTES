# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) #  {10 : 20 , 30 : 40 , 50 : 60}
a . clear() # clears all the elements in dict
print(a) # {}
del  a
#print(a) # error as dict is deleted



'''
What  is  the  differencee  betweeen   dict . clear()  and  del  dict ?  --->
														dict . clear()  removes  all  the  key : value  pairs  of  dictionary
														but  del  dict  deletes  dictionary  itself
'''

'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list

Eg:  List  'a'   --->  [10,20,30,40,50]   10,20,30,40,50,60,70,80
       List  'b'   --->  [5,12,20,37]   #5,12,20,37,40,45,65,80
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint :  Unsorted  lists  can  not  be  merged
'''

a=list(map(int,input("enter the elements in list1:").split(',')))
b=list(map(int,input("enter the elements in list1:").split(',')))
mergedlist = []
i,j=0,0
while i<len(a) and j<len(b) :
    if a[i]<b[j]:
        mergedlist.append(a[i])#[
        i+=1
    else:
        mergedlist.append(b[j])#[
        j+=1

mergedlist.extend(a[i:])
mergedlist.extend(b[j:])
print(mergedlist)



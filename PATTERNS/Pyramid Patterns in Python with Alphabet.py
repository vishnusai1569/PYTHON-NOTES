n=5
a=65
for i in range(0,n):
    print(" "*(n-i),end="")
    for j in range(0,i+1):
        print(chr(a),end=" ")
        a+=1
    print()
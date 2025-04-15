n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print(j+1,end="")
    print()

'''for i in range(1, rows + 1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print numbers
        for j in range(2 * i - 1):
            print(j + 1, end="")
        # Move to the next line after each row
        print()'''
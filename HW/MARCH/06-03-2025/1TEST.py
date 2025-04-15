acc_no=12345
name="ROHITH"
money=4856978
print("Wellcome To State Bank of India","\nenter 1 for withdraw","\nenter 2 for balance","\nenter 3 for exit")
k=int(input("enter a number:"))
if k==1:
    print("hello",name,"\nbalance",money)
    p=float(input("enter amount to withdraw:"))
    x=money-p
    print(f"withdrawl of {p} is sucessfull","\nnew account balance after withdraw:",x)
elif k==2:
    print("enter the money to withdraw in terms of 500 Rupees")
    l=int(input("Enter the amount"))
elif k==3:
    print("Thanks for using State Bank of India")
else:
    print("enter a valid input from 1 to 3")

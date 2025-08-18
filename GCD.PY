A=int(input("enter a number"))
B=int(input("enter a number"))
while(B!=0):
    rem=A%B
    A=B
    B=rem
print(A)

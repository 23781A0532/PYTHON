def k(a,b):
    if a==1:
        return
    while a%b!=0:
        b+=1
    print(b,end=" ")
    k(a//b,b)

n=int(input("Enter the number:"))
k(n,2)
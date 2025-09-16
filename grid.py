x=int(input("Enter number:"))
n=[["A" for i in range(x+2)]for j in range(x+2)]
for i in range(x+2):
    for j in range(x+2):
        if i==0 or i==x+1 or j==0 or j==x+1:
            n[i][j]="A"
        elif i%2!=0:
            n[i][j]="*"
        elif(i%2==0):
            n[i][j]="$"
for i in range(x+2):
    for j in range(x+2):
        print(n[i][j],end=" ")
    print()
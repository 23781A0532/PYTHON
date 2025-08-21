x=input(" enter a no")
n=201
c=0
for i in range(100,n):
    b=str(i)
    if (b==b[::-1]):
        c +=1
        print(c,")",b)
if x==c:
    print(x,b)
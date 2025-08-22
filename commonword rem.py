a=input("Enter name of a boy:")
b=input("Enter name of a girl:")
a1=list(a)
b1=list(b)
for i in range(len(a)):
    for j in range(len(b)):
        if(a1[i]==b1[j]):
            a1[i]='2'
            b1[j]='2'
print(a1)
print(b1)
c=0
for i in (a1):
    if(i!=2):
        c=c+1
for i in (b1):
    if(i!=2):
        c=c+1
print(c)

f=0
res=list("FLAMES")
for i in range(5):
    f=(f+(c-1))%len(res)
print(res[f])

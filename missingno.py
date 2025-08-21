#find the missing number
input=[1,2,4,5,6]
output=3 

a=[1,2,4,5,6]
unique=[]
for i in range(1,7):
    if i not in a:
        unique.append(i)
print(unique)




'''
n=5
s=1
for i in range(n):
    for j in range(i+1):
        print(s,end=" ")
        s +=1
    print()

 '''   
''' to find given 2 strings are anagrams


str1='liten'
str2='silent'
if str1 not in str2:
    print("Not anagram")
else:
    print("Anagram")
s='Narayana'
m=s[0]
c=0
a=" "
for i in s:
    if m==i:
        c+=1
    else:
        a+=m
        a+=str(c)
        m=i
        c=1
    print(a)

x=input("")
n=10
for i in range(1,n):
    if x in i:
        print(f"{x}){x**2}")
    print(f"{i}){i**2}")


to print palindrome numbers with serial numbers from 100 to 200
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
'''
    
    






























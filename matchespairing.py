import random
no=int(input("Enter no of teams:"))
teams=[]
for i in range(no):
    d=input("Enter team names:")
    teams.append(d)
meet=int(input("Enter number of meets:"))
matches=[]
for i in range(no-1):
    for j in range(i+1,no):
        for k in range(meet):
            matches.append([teams[i],teams[j]])
random.shuffle(matches)
for i in range(len(matches)):
    print(f"matches{i+1}:{matches[i][0]}vs{matches[i][1]}")


    #print("match{ } : { } vs { }".format(i+1,matches[i][0],matches[i][1]))
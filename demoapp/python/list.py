N = int(input())
lis=list()
for _ in range(N):
    s=input().strip().split(" ")
    if s[0]=="insert":
        lis.insert(int(s[1]),int(s[2]))
    if s[0]=="print":
        print(lis)
    if s[0]=="remove":
        lis.remove(int(s[1]))
    if s[0]=="append":
        lis.append(int(s[1]))
    if s[0]=="sort":
        lis.sort()
    if s[0]=="pop":
        lis.pop()
    if s[0]=="reverse":
        lis.reverse()
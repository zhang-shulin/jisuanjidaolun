i=int(input())
l=[1,1,2,3]
for m in range(4,20):
    l.append(l[m-1]+l[m-2])
while i:
    n=int(input())
    print(l[n-1])
    i=i-1


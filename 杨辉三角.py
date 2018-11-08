def C(n,k):
    x=1
    y=1
    if k==0 :
        return(1)
    else:
        for i in range(n-k+1,n+1):
            x=x*i
        for j in range(1,k+1):
            y=y*j
        return int(x/y)
while True:
    l=int(input())
    for a in range(l):
        for b in range(a+1):
            print(C(a,b),end=' ')
        print(end='\n')
    print(end='\n')

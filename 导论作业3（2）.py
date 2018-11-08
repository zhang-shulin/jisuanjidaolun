n,m=input().split('/')
n,m=int(n),int(m)
l=[31,28,31,30,31,30,31,31,30,31,30,31]
if n==1:
    print('这是2018年的第%d天'%m)
else:
    sum=0
    for i in l[:n-1:]:
        sum=sum+i
    print('这是2018年的第%d天'%(sum+m))

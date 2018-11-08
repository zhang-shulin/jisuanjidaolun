import re
a,b,c=re.split(' | | | ',input())
a,b,c=int(a),int(b),int(c)
while a:
    if a==0:
        break
    elif a+b>c and a+c>b and b+c>a:
        print('Great,you are genius')
    else:
        print('oh,my hod!')
    a,b,c=re.split(' | | | ',input())
    a,b,c=int(a),int(b),int(c)

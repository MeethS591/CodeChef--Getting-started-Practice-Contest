a,b,c = map(int,input().split())

if a+b>c and b+c>a and a+c>b:
    if a==b==c:
        print(1)
    elif a==b or b==c or a==c:
        print(2)
    elif a!=b and b!=c and c!=a:
        print(3)
else:
    print(-1)
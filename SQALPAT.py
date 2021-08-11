n = int(input())

num1,num2= [1,10]
for i in range(1,n+1):
    if i%2!=0:
        for j in range(num1,num1+5):
            print(j,end=' ')
        num1 +=10
        print()
    else:
        for j in range(num2, num2-5,-1):
            print(j,end=' ')
        num2+=10
        print()
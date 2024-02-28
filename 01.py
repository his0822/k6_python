N = int(input())
x = "*"
y = " "
if (1 <= N <= 100):
    for i in range(1,N+1):
        print(y*(N-i)+x*i)
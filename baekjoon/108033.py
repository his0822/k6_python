import random

N =int(input("N:"))
M = int(input("M:"))

# 1 <= N <= 500,000 // 1 <= M <= 500,000 
# -10,000,000<= cardNum <= 10,000,000

if( 1 <= N <= 500000 and 1 <= M <= 500000):
    dict = {i: random.randint(-10000000,10000000) for i in range(1, N + 1)}


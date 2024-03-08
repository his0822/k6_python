import random

N = int(input("N:"))
M = int(input("M:"))

if 1 <= N <= 500000 and 1 <= M <= 500000:
    range_start = -10000000
    range_end = 10000000

   
    listN = random.sample(range(range_start, range_end + 1), N)
    listM = random.sample(range(range_start, range_end + 1), M)

    listT = [0] * N 
     
print("listN : " , listN)
print("listM : " , listM)

for idxN in range(N):
    if listN[idxN] in listM:
        listT[idxN] = 1

print("listT :", listT)
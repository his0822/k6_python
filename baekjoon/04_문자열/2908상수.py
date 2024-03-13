import sys

# N,k = map(int, input().split())
# data = list(map(int(), input().split()))
# print(sorted(data, reverse=True)[k-1])

# N = int(input())
# # print(sys.stdin.readlines())
# data = [int(d.rstrip()) for d in sys.stdin.readlines()]
# print(data)
# print(data.sort())

num1,num2 = input().split()
rev1 = int(num1[::-1])
rev2 = int(num2[::-1])

if (rev1 < rev2):
    print(rev2)
else:
    print(rev1)


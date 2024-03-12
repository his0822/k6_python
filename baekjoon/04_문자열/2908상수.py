import sys

# N,k = map(int, input().split())
# data = list(map(int(), input().split()))
# print(sorted(data, reverse=True)[k-1])

N = int(input())
# print(sys.stdin.readlines())
data = [int(d.rstrip()) for d in sys.stdin.readlines()]
print(data)
print(data.sort())
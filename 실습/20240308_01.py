def add(a,b):
    return a+b
print(add(1,2))

with open('name.txt') as file:
    for line in file:
        print(line, end='')
        print(line.rstrip())

print('A', end='\n') # print 메소드에는 기본적으로 ", end='\n'" 내용이 생략됨
print('B', end=' ') #띄어쓰기로 바꾸기 가능
print('A','B','C', sep='. ')

with open('name.txt') as file:
    for line in file.readlines():
        print(line.rstrip())

import csv

with open('grade.csv') as file:
    reader = csv.reader(file)
    header = next(reader)
    for line in reader:
        print(line)
    print(header)

n = range(10)
print(n)
r = iter(n)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))

for i in range(5):
    print(i)
      
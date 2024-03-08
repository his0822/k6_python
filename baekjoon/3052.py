import random

lst = []
for i in range(10):
    lst.append(random.randint(1,1000))
    lst[i]=lst[i%42]
    
for j in range(10)-i:
    for i in range(10):
        if(lst[i] == lst[i+j]):



# 교수님 예시---------------------------------------
data = []
for _ in range(10):
    data.append(int(input()) % 42)

answer=[]
for d in data:
    if d not in answer:
        answer.append(d)
print(answer)

for  i in range(10):
print(i%3, i/3)

print(set([1,1,1])) #set으로 묶으면 중복은 삭제



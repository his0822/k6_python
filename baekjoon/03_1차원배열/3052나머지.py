# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 
# 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

lst = []
for _ in range(10):
    lst.append(int(input())%42)
print(len(set(lst)))



# 교수님 예시---------------------------------------
# data = []
# for _ in range(10):
#     data.append(int(input()) % 42)

# answer=[]
# for d in data:
#     if d not in answer:
#         answer.append(d)
# print(answer)

# for  i in range(10):
#     print(i%3, i/3)

# print(set([1,1,1])) #set으로 묶으면 중복은 삭제



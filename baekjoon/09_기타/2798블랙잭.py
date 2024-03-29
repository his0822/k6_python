# 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다.
# 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다.
# 블랙잭은 카지노마다 다양한 규정이 있다.

# 한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.

# 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 
# 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다.
# 그런 후에 딜러는 숫자 M을 크게 외친다.

# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 
# 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

# N:총 카드갯수
# M:최대한 가깝게 맞춰야하는 수
# 카드숫자:양수

# -----------------------------------------------------------------

# N,M = map(int,input().split())
# print("N =",N,"M =",M)
# N_list= list(map(int,input().split()))
# print(N_list)
# tmp=0
# slist=[]
# for i in range(N):
#     for j in range(i+1,N):
#         for k in range(j+1,N):
#             sumset = (N_list[i]+N_list[j]+N_list[k])
#             if( (sumset <= M) and (sumset > max(tmp)) ):
#                 tmp = sumset
#                 slist = sumset
#                 print("[",N_list[i], N_list[j], N_list[k],"]")
# print("최종:",max(tmp))

# ======================================================================///
# 완성코드
# N, M = map(int, input().split())
# print("N =", N, "M =", M)
# N_list = list(map(int, input().split()))
# print(N_list)

# max_sum = 0
# max_subset = []

# # 세 요소의 조합 찾기
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             subset_sum = N_list[i] + N_list[j] + N_list[k]
#             if subset_sum <= M and subset_sum > max_sum:
#                 max_sum = subset_sum
#                 max_subset = [N_list[i], N_list[j], N_list[k]]

# # 최대 합과 해당 요소들 출력
# if max_subset:
#     print("최대 합:", max_sum, "요소 :", max_subset)  
# else:
#     print("M 이하의 합을 가지는 조합을 찾을 수 없습니다.")

# ====================================================================

N, M = map(int, input().split())
# print("N =", N, "M =", M)
N_list = list(map(int, input().split()))
# print(N_list)

max_sum = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            subset_sum = N_list[i] + N_list[j] + N_list[k]
            if subset_sum <= M and subset_sum > max_sum:
                max_sum = subset_sum

print (max_sum)  

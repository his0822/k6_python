# 그룹 단어 체커

# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.


n = int(input())
cnt = 0

for i in range(n):
    words = input()
    bow=[]
    if len(words)==1:
        cnt +=1
    else:
        for j in range(len(words)):
            if j == 0:
                bow.append(words[0])
            elif j > 0:
                if words[j] == words[j-1]:
                    bow.append(words[j])
                    if j == len(words)-1:
                        cnt += 1
                    
                elif words[j] != words[j-1]: # j번째 철자가 앞의 철자와 다를 때
                    if words[j] not in bow:
                        if j == len(words)-1:
                            cnt += 1
                        else:
                            bow.append(words[j])
                    elif words[j] in bow: # j번째 철자가 앞에서 등장했다면 중단
                        break
                

print(cnt)


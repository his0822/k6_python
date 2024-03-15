#  알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.



M,N = map(int, input().split())
print(M,N)
A= [list(map(int, input.split())) for _ in range(M)] 
B= [list(map(int, input.split())) for _ in range(N)]



for a,b in zip(A,B):
    print(' '.join([str(a[i]+b[i]) for i in range(M)]))

import numpy as np
print(np.array(a)+np.array(B))
# <그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 
# 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

# table = [list(map(int, input().split())) for _ in range(9)]

# max_num = 0
# max_row, max_col = 0, 0
# for row in range(9):
#     for col in range(9):
#         if max_num <= table[row][col]:
#             max_row = row + 1
#             max_col = col + 1
#             max_num = table[row][col]

# print(max_num)
# print(max_row, max_col)



tb = [list(map(int, input().split())) for _ in range(9)]

maxnum, rownum, colnum = 0,0,0

for row in range(9):
    for col in range(9):
        if maxnum <= tb[row][col]:
            rownum = row+1
            colnum = col+1
            maxnum = tb[row][col]

print(maxnum)
print(rownum,colnum)
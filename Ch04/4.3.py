# for value in range(1,5):
#     print(value)
# print("---------------------")
# for value in range(1,6):
#     print(value)
# print("---------------------")
# for i in range(6):
#     print(i+1)

# numbers = list[range(1,6)]
# print(numbers)


# numbers3 = list(range(1,10,2))

# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)

# squares = [value ** 2 for value in range(1,11) ]
# print(squares)
# print(value)
# print(squares[2:4])
# print(squares[:3])
# print(squares[2:])
# print(squares[-3:])
# print(squares[:])

# mlist = [1,2,3,4,5,6,7,8]
# print(mlist[::-3])
a = [1,2,3,4]
b = [3,4]
c1 = list(set(a)-set(b))
c2 = [x for x in a if x not in b]
print(c1)
print(c2)


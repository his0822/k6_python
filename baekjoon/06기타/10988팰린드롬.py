word1 = [list for _ in (input().split())]
word2 = [w[::-1] for w in word1]

print(word1)
print(word2)
w1 = "".join(word1)
w2 = "".join(word2)
if( w1 == w2):
 print(1)
else:
 print(0)
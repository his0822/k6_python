#  알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.


# word = input().upper()
# word_list = list(set(word))

# lst = []
# for i in word_list:
#     count = word.count(i)
#     lst.append(count)

# if lst.count(max(lst))>= 2:
#     print("?")
# else:
#     print(word_list[lst.index(max(lst))])




word = input().upper()
word_list = list(set(word))

lst=[]
for i in word_list:
    cnum = word.count(i)
    lst.append(cnum)

if lst.count(max(lst))>=2 :
    print("?")
else:
    print(word_list[lst.index(max(lst))])
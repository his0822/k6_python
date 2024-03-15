import matplotlib.pyplot as plt

# x1 = list(range(5))
# y1 = [i**2 for i in x1]

# x2 = list(range(5))
# y2 = [i**3 for i in x2]

# fig, ax = plt.sublots()
# ax.plot(x1,y1, label='AAA', color = "red")
# ax.plot(x2,y2, label='BBB', color = "black")
# ax.scatter(x1,y1, color="red")
# ax.set_title('AAA vs BBB')
# ax.set_xlabel('x1')
# ax.set_ylabel('y1')

# plt.legend()
# plt.show()

# data = {"이름":["국어","영어"], "홍길동": [50, 30] ,"이순신":[70,50],"강감찬":[20,70]}
data = {"이름":["홍길동","이순신","강감찬"],"국어":[50,70,20],"영어":[30,50,70]}
names = data["이름"]
# scores = {subject: scores for subject, scores in data.items() if subject != "이름"}
scores = {}
for subject, score in data.items():
    if subject != "이름":
        scores[subject] = score


fix, ax = plt.subplots()

for subject, score in scores.items():
    ax.plot(names, score, marker='o', label=subject)
ax.set_title("시험결과")
ax.legend()

plt.show()

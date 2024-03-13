import matplotlib.pyplot as plt


x = list(range(1,101))
print(len(x))
square = [i**2 for i in x]
# squares = list(map(lambda i: i**2, x))
fig, ax = plt.subplots()
# ax.plot(x, square)
ax.scatter(x, square)
ax.set_title('Squares')
ax.set_xlabel('X')
ax.set_ylabel('Y')
# ax.tick_params(labelsize=30)
# ax.set_xlim(0,20)
# ax.set_ylim(0,20)
# plt.style.use('seaborn-v0_8-pastel')
# ax.ticklabel_format(style = 'plain')

for s in plt.style.available:
    print(s)

plt.show()
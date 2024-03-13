import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # Create a figure containing a single axes.
x1 = [1, 2, 3, 4]
y1 = [2, 3, 4, 6]
ax.plot(x1, y1, label = 'blue')  # Plot some data on the axes.

x2 = [2, 3, 4, 6]
y2 = [1, 2, 3, 4]
# ax.scatter(x1,y2, label = 'black')
ax.plot(x2, y2 ,label = 'yellow')

ax.set_aspect('equal')
ax.set_title('Plot A and B')
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.set_xlabel('Age')   
ax.set_ylabel('BMI')
ax.legend() #이미지 라벨표시
plt.savefig('plot.png') #이미지 저장
plt.show()
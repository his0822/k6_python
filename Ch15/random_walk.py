import random
import matplotlib.pyplot as plt

x = [random.randint(0,100) for _ in range(100)]
y = [random.randint(100,200) for _ in range(100)]

x_walks = [5,-5]
y_walks = [5,-5]
x,y, = 0,0
x_data,y_data =[],[]
x_data.append(x)
x_data.append(x)

# for x , y in zip(x_walks, y_walks):
#     print(x,y)
random_walks = [[-5,5,-5,5][random.randin(0,4)] for _ in range(100)]

for x_move, y_move in zip(x_walks,y_walks):
    x,y = x+x_move, y+y_move
    x_data.append(x)
    y_data.append(y)

fig, ax = plt.subplots()
ax.plot(x_data,y_data)
# ax.plot(x[:50],y[:50], color ="red")
# ax.plot(x[50:],y[50:], color ="blue")

# ax.scatter(x[:50],y[:50], color ="red")
# ax.scatter(x[50:],y[50:], color ="blue")
# print(x,y)

plt.show()


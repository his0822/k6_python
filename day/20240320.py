from matplotlib import pyplot as plt
from random import randint
import csv
from datetime import datetime

x1,x2,y1,y2=[],[],[],[]


with open('a.csv','r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        print(type( datetime.strptime ( row[2] , '%Y-%m-%d' ) ), type(row[4]), type(row[5]))
        x1.append(datetime.strptime (row[2] , '%Y-%m-%d'))
        y1.append(int(row[4]))
        y2.append(int(row[5]))
        
plt.plot(x1,y1, label='TMAX', color='red')
plt.plot(x1,y2, label='TMIN', color='blue')
plt.fill_between(x1,y1,y2,alpha=0.5)

# x1 = list(range(1,5))
# y1= [i*i for i in x1]

# x2 = list(range(1,5))
# y2= [i**3 for i in x2]

# fig, axs = plt.subplots(1,2)

# # print(x1, type(x1))
# # print(y1, type(y1))


# x1 = []
# y1 = []

# plt.plot(x1,y1, label='A', color='red')
# axs[0].plt.plot(x2,y2, label='B', color='blue')

# axs[1].plt.plot(x1,y1, label='A', color='red')
# axs[1].plt.plot(x2,y2, label='B', color='blue')

# plt.title('X Square')
# plt.xlabel('X')
# plt.ylabel('X Square')

plt.xticks( x1, rotation = 'vertical')
plt.xlabel('Date')
plt.legend()
plt.show()
# with open('a.csv') as f:
#     for line in f:
#         print(line.rstrip().split(','))
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import csv
import json
import platform
sys_font=fm.findSystemFonts()
print(sys_font)
# plt.rc('font', family='Malgun Gothic')
# plt.reParams['axes.unicode_minus'] = False

x1,y1 = [],[]
x2,y2 = [],[]


COL_DATA = 2
COL_TMAX = 4

with open('a.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        # print(line, type(line))
        
        x1.append(line[COL_DATA])
        
        y1.append(line[COL_TMAX])

        x2.append(line[2])
        y2.append(line[5])



# plt.title('TMAX')
plt.plot(x1,y1, label = 'TMAX')
plt.plot(x2,y2, label = 'TMIN')
plt.xticks(rotation = 90)
plt.legend()
plt.show()

import datetime
from datetime import datetime as dt

today = dt.strptime('2024-03-15', '%Y-%m-%d')

print(today, type(today), type('2024-03-15'))

# print(today + datetime.timedelta(days=3))
# print(datetime(2024,3,14))
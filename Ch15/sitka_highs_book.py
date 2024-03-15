from pathlib import Path
import csv
from datetime import datetime as dt
import matplotlib.pyplot as plt

print(plt.style.available)


path = Path('a.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

dates, highs = [],[]
for row in reader:
    current_date =dt.strptime(row[2], '%Y-%m-%d')
    high = int (row[4])
    dates.append(current_date)
    highs.append(high)


fig,ax = plt.subplots()
ax.plot(dates, highs, color='red')

plt.style.use('seaborn-v0_8-whitegrid')
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel("",fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
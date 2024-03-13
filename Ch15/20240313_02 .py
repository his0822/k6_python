import matplotlib.pyplot as plt
import random

fig, ax = plt.subplots()  # Create a figure containing a single axes.

data = [random.randint(0,100) for I in range(1000)]
print(data)
ax.hist(data)

plt.show()
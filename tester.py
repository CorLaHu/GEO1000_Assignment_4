from time import perf_counter
from os import system
import subprocess
import matplotlib.pyplot as plt
import numpy as np

nbodypy = r"C:\Users\ordin\Documents\Github\GEO1000_Assignment_4\nbody.py"
nbodyexe = r"C:\Users\ordin\Documents\Github\GEO1000_Assignment_4\cmake-build-release\nbody.exe"
iterations = [5000, 500000, 5000000]
ctimes = []
pytimes = []

for iteration in iterations:
	print(f"Currently running iteration number {iteration} in C++")
	t1 = perf_counter()
	system(f"{nbodyexe} {iteration}")
	t2 = perf_counter()
	ctimes.append(t2 - t1)

for iteration in iterations:
	print(f"Currently running iteration number {iteration} in Python")
	t1 = perf_counter()
	system(f"python {nbodypy} {iteration}")
	t2 = perf_counter()
	pytimes.append(t2 - t1)

print(ctimes)
print(pytimes)


labels = ["5000", "500000", "5000000"]
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, ctimes, width, label='C++')
rects2 = ax.bar(x + width/2, pytimes, width, label='Python')
plt.yscale('log')

ax.set_ylabel('Runtime in seconds')
ax.set_xlabel('Instance size')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.savefig("exportgraph.png")
from time import perf_counter
from os import system
import subprocess
import matplotlib.pyplot as plt
import numpy as np

nbodypy = r"C:\Users\Durspy\Documents\GitHub\GEO1000_Assignment_4\nbody.py"
nbodyrelexe = r"C:\Users\Durspy\Documents\GitHub\GEO1000_Assignment_4\cmake-build-release\nbody.exe"
nbodydebexe = r"C:\Users\Durspy\Documents\GitHub\GEO1000_Assignment_4\cmake-build-debug\nbody.exe"
iterations = [5000, 500000, 5000000, 50000000]

creltimes = []
cdebtimes = []
pytimes = []

for iteration in iterations:
	print(f"Currently running iteration size number {iteration} in C++ debug build")
	t1 = perf_counter()
	system(f"{nbodydebexe} {iteration}")
	t2 = perf_counter()
	cdebtimes.append(t2 - t1)

for iteration in iterations:
	print(f"Currently running iteration size number {iteration} in C++ release build")
	t1 = perf_counter()
	system(f"{nbodyrelexe} {iteration}")
	t2 = perf_counter()
	creltimes.append(t2 - t1)


for iteration in iterations:
	print(f"Currently running iteration size number {iteration} in Python")
	t1 = perf_counter()
	system(f"python {nbodypy} {iteration}")
	t2 = perf_counter()
	pytimes.append(t2 - t1)

print(cdebtimes)
print(creltimes)
print(pytimes)

for (a, b, c, i) in zip(cdebtimes, creltimes, pytimes, range(len(iterations))):
	cdebtimes[i] = round(a, 3)
	creltimes[i] = round(b, 3)
	pytimes[i] = round(c, 3)

print(cdebtimes)
print(creltimes)
print(pytimes)


labels = ["5000", "500000", "5000000", "50000000"]
x = np.arange(len(labels))
width = 0.28
fig, ax = plt.subplots()
rects1 = ax.bar(x - width, cdebtimes, width, label='C++ Debug')
rects2 = ax.bar(x, creltimes, width, label='C++ Release')
rects3 = ax.bar(x + width, pytimes, width, label='Python')
plt.yscale('log')

ax.set_ylabel('Runtime in log(seconds)')
ax.set_xlabel('Instance size')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=4)
ax.bar_label(rects2, padding=4)
ax.bar_label(rects3, padding=4)


fig.tight_layout()

plt.savefig("exportgraph.png")
from time import perf_counter
from os import system
import subprocess

nbodypy = r"C:\Users\ordin\Documents\Github\GEO1000_Assignment_4\nbody.py"
nbodyexe = r"C:\Users\ordin\Documents\Github\GEO1000_Assignment_4\cmake-build-release\nbody.exe"
iterations = [5000, 500000, 5000000]

times = {"c": [], "py": []}

for iteration in iterations:
	print(f"Currently running iteration number {iteration} in C++")
	t1 = perf_counter()
	system(f"{nbodyexe} {iteration}")
	t2 = perf_counter()
	times["c"].append(t2 - t1)

for iteration in iterations:
	print(f"Currently running iteration number {iteration} in Python")
	t1 = perf_counter()
	system(f"python {nbodypy} {iteration}")
	t2 = perf_counter()
	times["py"].append(t2 - t1)

print(times["c"])
print(times["py"])

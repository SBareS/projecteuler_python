"""Test the solution for the problems. Each solution is expected to be 
in a python file problemN.py where N = 1, 2, ... . When the file is 
run, it should output the answer to stdio as the last line of its 
output. Additionally, to be tested, the module must contain a variable
correct_answer of type str, against which the answer is to be compared."""

from contextlib import redirect_stdout
from heapq import nlargest
import importlib
from io import StringIO
import os
import re
from time import perf_counter

files = [f for f in os.listdir() if re.match(r"problem\d+.py", f)]
files.sort(key=lambda f: int(re.match(r"problem(\d+).py", f).group(1)))

times = {}
n_passed = 0
failed_tests = []
for file in files:
    modname = file[:-3]
    print(f"Testing {modname}... ", end='')
    with redirect_stdout(StringIO()) as f:
        t0 = perf_counter()
        mod = importlib.import_module(modname)
        t1 = perf_counter()
        times[modname] = t1 - t0
        f.seek(0)
        output_lines = list(map(lambda s: s.strip(), f.readlines()))
    
    if output_lines[-1] == mod.correct_answer:
        print("OK")
        n_passed += 1
    else:
        print(f"FAILED: expected {mod.correct_answer} but got {output_lines[-1]}")
        failed_tests.append(modname)

print(f"{n_passed}/{len(files)} tests passed.")
if failed_tests:
    print("The following problem(s) failed: ", end='')
    print(*failed_tests, sep=" , ")

over_one_minute = [k for k, v in times.items() if v > 60]
if over_one_minute:
    print("The following problems took longer than one minute:")
    print(*over_one_minute, sep=" , ")
else:
    print("All problems solved in less than one minute.")

print("These are the 10 slowest solutions:")
for k, v in nlargest(10, times.items(), key=lambda x: x[1]):
    print(f"{k:<16}{v:.1f} seconds")
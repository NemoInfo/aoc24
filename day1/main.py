import numpy as np

file = open("input.txt", "r")

###############*###############
#           PART 1            #
###############*###############
nums = np.array([[*map(int,
                       line.strip().split("   "))]
                 for line in file.readlines()])
snums = np.sort(nums, axis=0)
res1 = abs(snums[:, 0] - snums[:, 1]).sum()

print(f"Part 1: {res1}")

###############*###############
#           PART 2            #
###############*###############
f1, f2 = {}, {}
for a, b in nums:
  f1[a] = (f1.get(a) or 0) + 1
  f2[b] = (f2.get(b) or 0) + 1

res2 = 0
for n, c in f1.items():
  res2 += c * n * (f2.get(n) or 0)

print(f"Part 2: {res2}")

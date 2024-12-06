import numpy as np

file = open("input.txt", "r")
nums = [np.array([*map(int, line.strip().split())]) \
        for line in file.readlines()]

###############*###############
#           PART 1            #
###############*###############
res1 = 0
for xs in nums:
  ds = xs[:-1] - xs[1:]
  if all(abs(ds) >= 1) & all(abs(ds) <= 3) & \
    (all(ds > 0) | all(ds < 0)):
    res1 += 1

print(f"Part 1: {res1}")

###############*###############
#           PART 2            #
###############*###############
res2 = 0
for xs in nums:
  for i in range(len(xs)):
    ys = np.append(xs[:i], xs[i + 1:])
    ds = ys[:-1] - ys[1:]
    if all(abs(ds) >= 1) & all(abs(ds) <= 3) & \
      (all(ds > 0) | all(ds < 0)):
      res2 += 1
      break

print(f"Part 2: {res2}")

import numpy as np
from itertools import zip_longest

FILENAME = "input.txt"

###############*###############
#           PART 1            #
###############*###############
file = open(FILENAME, "r")
nums = np.array(list(zip_longest(*[[*map(int, \
                  line.strip().split(" "))] for line in file.readlines()],
                fillvalue=np.nan))).T

diff = nums[:, :-1] - nums[:, 1:]
nans = np.isnan(diff)

res1 = (np.all(nans | (abs(diff) >= 1) & (abs(diff) <= 3), axis=1)
        & (np.all(nans | (diff > 0), axis=1)
           | np.all(nans | (diff < 0), axis=1))).sum()

print(f"Part 1: {res1}")

###############*###############
#           PART 2            #
###############*###############
file = open(FILENAME, "r")
nums = [
    np.array([*map(int,
                   line.strip().split())]) for line in file.readlines()
]

res2 = 0
for xs in nums:
  for i in range(len(xs)):
    ys = np.append(xs[:i], xs[i + 1:])
    ds = ys[:-1] - ys[1:]
    if np.all(abs(ds) >= 1) & np.all(abs(ds) <= 3) & \
      (np.all(ds > 0) | np.all(ds < 0)):
      res2 += 1
      break

print(f"Part 2: {res2}")

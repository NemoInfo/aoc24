import numpy as np
from itertools import combinations

grid = np.array([[*line]
                 for line in open("input.txt", "r").read().splitlines()])

###############*###############
#           PART 1            #
###############*###############
antenas = {}
for ij, c in np.ndenumerate(grid):
  if c == '.': continue
  antenas[c] = antenas.get(c, []) + [np.array(ij)]

antinodes = set()
for k, ijs in antenas.items():
  for p1, p2 in combinations(ijs, 2):
    dp = p1 - p2
    if all(p1 + dp >= 0) and all(p1 + dp < grid.shape):
      antinodes.add(tuple(p1 + dp))
    if all(p2 - dp >= 0) and all(p2 - dp < grid.shape):
      antinodes.add(tuple(p2 - dp))

print(f"Part 1: {len(antinodes)}")
###############*###############
#           PART 2            #
###############*###############

for k, ijs in antenas.items():
  for p1, p2 in combinations(ijs, 2):
    dp = p1 - p2
    while all(p1 + dp >= 0) and all(p1 + dp < grid.shape):
      p1 = p1 + dp
      grid[*p1] = "#"
    while all(p2 - dp >= 0) and all(p2 - dp < grid.shape):
      p2 = p2 - dp
      grid[*p2] = "#"

res2 = len(np.where(grid != ".")[0])
print(f"Part 2: {res2}")

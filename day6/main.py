import numpy as np
from tqdm import tqdm

file = open("input.txt", "r")
grid = np.array([*map(list, file.read().splitlines())])

sr, sc = 0, 0
for sr, sc in np.ndindex(*grid.shape):
  if grid[sr, sc] == "^":
    break

###############*###############
#           PART 1            #
###############*###############
seen = set()
dr, dc = -1, 0
r, c = sr, sc
while True:
  seen.add((r, c))
  if not 0 <= r + dr < grid.shape[0] or not 0 <= c + dc < grid.shape[1]:
    break
  if grid[r + dr, c + dc] == "#":
    dc, dr = -dr, dc
  else:
    r, c = r + dr, c + dc

print(f"Part 1: {len(seen)}")


###############*###############
#           PART 2            #
###############*###############
def loops(grid):
  seen = set()
  dr, dc = -1, 0
  r, c = sr, sc
  while True:
    seen.add((r, c, dr, dc))
    if not 0 <= r + dr < grid.shape[0] or not 0 <= c + dc < grid.shape[1]:
      return False
    if grid[r + dr, c + dc] == "#":
      dc, dr = -dr, dc
    else:
      r, c = r + dr, c + dc
    if (r, c, dr, dc) in seen:
      return True


res2 = 0
for r, c in tqdm(seen, colour='#4DAED3', ncols=100, \
                 leave=False, desc="Checking obstacles"):
  if grid[r, c] != ".": continue
  grid[r, c] = "#"
  if loops(grid):
    res2 += 1
  grid[r, c] = "."

print(f"Part 2: {res2}")

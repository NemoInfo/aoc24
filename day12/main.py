import numpy as np

chr_grid = np.array([[*line.strip()] for line in open("input.txt", "r")])
int_grid = -np.ones(chr_grid.shape)


def flood(new_grid, src_grid, i, j, idx):
  new_grid[i, j] = idx
  for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    ni, nj = i + di, j + dj
    if 0 <= ni < src_grid.shape[0] and 0 <= nj < src_grid.shape[0] and \
        src_grid[i, j] == src_grid[ni, nj] and new_grid[ni, nj] == -1:
      flood(new_grid, src_grid, ni, nj, idx)


idx = 0
for (i, j), c in np.ndenumerate(int_grid):
  if c == -1:
    flood(int_grid, chr_grid, i, j, idx)
    idx += 1

areas = {}
for c in int_grid.flat:
  areas[c] = areas.get(c, 0) + 1


###############*###############
#           PART 1            #
###############*###############
def half_perimeter(perimeter, grid):
  for line in grid:
    perimeter[line[0]] += 1
    perimeter[line[-1]] += 1
    for c1, c2 in zip(line[:-1], line[1:]):
      if c1 != c2:
        perimeter[c1] += 1
        perimeter[c2] += 1


perimeter = {c: 0 for c in areas.keys()}
half_perimeter(perimeter, int_grid)
half_perimeter(perimeter, int_grid.T)

res1 = 0
for c in perimeter.keys():
  res1 += perimeter[c] * areas[c]

print(f"Part 1: {res1}")

###############*###############
#           PART 2            #
###############*###############
pad_grid = -np.ones((int_grid.shape[0] + 2, int_grid.shape[1] + 2))
pad_grid[1:-1, 1:-1] = int_grid

sides = {c: 0 for c in areas.keys()}
sides[-1] = 0

# c0 c1
# c2 c3
for cs in zip(pad_grid[:-1, :-1].flat, pad_grid[:-1, 1:].flat, \
              pad_grid[1:, :-1].flat, pad_grid[1:, 1:].flat):
  counts = {}
  for c in cs:
    counts[c] = counts.get(c, 0) + 1

  for k, v in counts.items():
    if v % 2:
      sides[k] += 1
    elif v == 2 and (cs[0] == cs[3] or cs[1] == cs[2]):
      sides[k] += 2

res2 = 0
for c in areas.keys():
  res2 += sides[c] * areas[c]

print(f"Part 2: {res2}")

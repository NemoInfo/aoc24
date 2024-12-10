from numpy import ndindex

grid = [[*map(int, line[:-1])] for line in open("input.txt", "r")]
rows, cols = len(grid), len(grid[0])

###############*###############
#           PART 1            #
###############*###############


def count_heads(r, c):
  s = set()
  if grid[r][c] == 9: s.add((r, c))
  for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
    if 0 <= r + dr < rows and 0 <= c + dc < cols and \
      grid[r + dr][c + dc] - 1 == grid[r][c]:
      s.update(count_heads(r + dr, c + dc))
  return s


res1 = 0
for r, c in ndindex(rows, cols):
  if grid[r][c] == 0: res1 += len(count_heads(r, c))

print(f"Part 1: {res1}")
###############*###############
#           PART 2            #
###############*###############


def count_paths(r, c):
  if grid[r][c] == 9: return 1
  s = 0
  for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
    if 0 <= r + dr < rows and 0 <= c + dc < cols and \
        grid[r + dr][c + dc] - 1 == grid[r][c]:
      s += count_paths(r + dr, c + dc)
  return s


res2 = 0
for r, c in ndindex(rows, cols):
  if grid[r][c] == 0: res2 += count_paths(r, c)

print(f"Part 2: {res2}")

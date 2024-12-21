grid = open("input.txt").read().splitlines()
rows = len(grid)
cols = len(grid[0])

sr = sc = 0
for sr, row in enumerate(grid):
  for sc, ch in enumerate(row):
    if ch == "S": break
  else: continue
  break

###############*###############
#           PART 1            #
###############*###############
d = [[float('inf')] * cols for _ in range(rows)]
d[sr][sc] = 0

r, c = sr, sc
while grid[r][c] != "E":
  for nr, nc in [[r, c + 1], [r + 1, c], [r, c - 1], [r - 1, c]]:
    if grid[nr][nc] != "#" and d[nr][nc] == float('inf'):
      d[nr][nc] = d[r][c] + 1
      r, c = nr, nc

res1 = 0
for r, row in enumerate(grid):
  for c, ch in enumerate(row):
    if ch == "#": continue
    for nr, nc in [[r, c + 2], [r + 1, c + 1], [r + 2, c], [r + 1, c - 1]]:
      res1 += int(0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#"
                  and abs(d[r][c] - d[nr][nc]) - 2 >= 100)

print("Part 1:", res1)
###############*###############
#           PART 2            #
###############*###############
cheats = []
for dr in range(-20, 21):
  for dc in range(-20, 21):
    if ((dc >= 0 and dr > 0) or (dc >= 1 and dr <= 0)) and \
      1 < abs(dr) + abs(dc) <= 20:
      cheats.append((dr, dc, abs(dr) + abs(dc)))

res2 = 0
for r, row in enumerate(grid):
  for c, ch in enumerate(row):
    if ch == "#": continue
    for dr, dc, ps in cheats:
      nr, nc = r + dr, c + dc
      res2 += int(0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#"
                  and abs(d[r][c] - d[nr][nc]) - ps >= 100)

print("Part 2:", res2)

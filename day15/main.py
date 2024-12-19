grid, moves = open("input.txt", "r").read().strip().split("\n\n")

grid = [list(line) for line in grid.splitlines()]
original_grid = [row.copy() for row in grid]

decode_move = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
moves = list(map(lambda m: decode_move[m], moves.replace("\n", "")))

###############*###############
#           PART 1            #
###############*###############

sr = sc = 0
for sr, row in enumerate(grid):
  for sc, val in enumerate(row):
    if val == "@": break
  else:
    continue
  break

for dr, dc in moves:
  nr, nc = sr + dr, sc + dc
  while grid[nr][nc] == "O":
    nr, nc = nr + dr, nc + dc
  if grid[nr][nc] == "#":
    continue
  while nr != sr + dr or nc != sc + dc:
    grid[nr][nc] = "O"
    nr, nc = nr - dr, nc - dc
  grid[sr][sc] = "."
  sr, sc = nr, nc
  grid[sr][sc] = "@"

res1 = 0
for r, row in enumerate(grid):
  for c, val in enumerate(row):
    if val == "O": res1 += 100 * r + c

print("\n".join(["".join(row) for row in grid]))
print(f"Part 1: {res1}")

###############*###############
#           PART 2            #
###############*###############
grid = original_grid

grid = ["".join(line). \
        replace(".", ".."). \
        replace("#", "##"). \
        replace("O", "[]"). \
        replace("@", "@.") for line in grid]

grid = [list(row) for row in grid]

for sr, row in enumerate(grid):
  for sc, val in enumerate(row):
    if val == "@": break
  else:
    continue
  break

for dr, dc in moves:
  targets = [(sr, sc)]
  i = 0
  while i < len(targets):
    nr, nc = targets[i]
    if grid[nr][nc] == "#": break
    if grid[nr][nc] == ".":
      targets.pop(i)
      continue
    if (nr + dr, nc + dc) not in targets:
      targets += [(nr + dr, nc + dc)]
    if grid[nr][nc] == "[" and (nr, nc + 1) not in targets:
      targets += [(nr, nc + 1)]
    elif grid[nr][nc] == "]" and (nr, nc - 1) not in targets:
      targets += [(nr, nc - 1)]
    i += 1
  else:
    while targets:
      nr, nc = targets.pop()
      grid[nr + dr][nc + dc] = grid[nr][nc]
      grid[nr][nc] = "."
    sr, sc = sr + dr, sc + dc

print("\n".join(["".join(row) for row in grid]))

res2 = 0
for r, row in enumerate(grid):
  for c, val in enumerate(row):
    if val == "[": res2 += 100 * r + c

print(f"Part 2: {res2}")

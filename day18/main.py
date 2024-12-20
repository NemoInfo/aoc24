from collections import deque
from tqdm import tqdm

full = True
file = ["test.txt", "input.txt"][int(full)]
N = [7, 71][int(full)]
B = [12, 1024][int(full)]

###############*###############
#           PART 1            #
###############*###############
grid = [["."] * N for _ in range(N)]
for row in open(file).read().splitlines()[:B]:
  c, r = map(int, row.strip().split(","))
  grid[r][c] = "#"

q = deque([(0, 0, 0)])
seen = set()
cost = float("inf")
while q:
  cost, r, c = q.popleft()
  if (r, c) in seen:
    continue
  seen.add((r, c))
  if r == c == N - 1:
    break
  for nr, nc in [[r, c + 1], [r + 1, c], [r, c - 1], [r - 1, c]]:
    if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == "." and \
        (nr, nc) not in seen:
      q.append((cost + 1, nr, nc))

print("Part 1:", cost)

###############*###############
#           PART 2            #
###############*###############


def check_path(grid):
  q = deque([(0, 0)])
  seen = set()
  while q:
    r, c = q.popleft()
    if (r, c) in seen: continue
    seen.add((r, c))
    if r == c == N - 1: break
    for nr, nc in [[r, c + 1], [r + 1, c], [r, c - 1], [r - 1, c]]:
      if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == "." and \
          (nr, nc) not in seen:
        q.append((nr, nc))
  else:
    return False
  return True


row = None
for row in tqdm(open(file).read().splitlines()[B:],
                leave=False,
                ncols=100,
                desc="Part 2"):
  c, r = map(int, row.strip().split(","))
  grid[r][c] = "#"
  if not check_path(grid):
    break

print("Part 2:", row)

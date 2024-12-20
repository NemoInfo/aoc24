import heapq

grid = [list(row.strip()) for row in open("input.txt")]

er = ec = sr = sc = 0
for r, row in enumerate(grid):
  for c, ch in enumerate(row):
    if ch == "E":
      er, ec = r, c
    elif ch == "S":
      sr, sc = r, c

###############*###############
#           PART 1            #
###############*###############
pq = [(0, sr, sc, 0, 1)]
best = {}
end_cost = float('inf')

while pq:
  cost, r, c, dr, dc = heapq.heappop(pq)
  if cost >= best.get((r, c, dr, dc), float("inf")):
    continue
  best[(r, c, dr, dc)] = cost
  if grid[r][c] == "E":
    end_cost = min(end_cost, cost)
    continue
  if grid[r + dr][c + dc] != "#":
    heapq.heappush(pq, (cost + 1, r + dr, c + dc, dr, dc))
  if grid[r - dc][c + dr] != "#":
    heapq.heappush(pq, (cost + 1000, r, c, -dc, dr))
  if grid[r + dc][c - dr] != "#":
    heapq.heappush(pq, (cost + 1000, r, c, dc, -dr))

print(f"Part 1: {end_cost}")
###############*###############
#           PART 2            #
###############*###############
seen = set()


def dfs(k, r, c, dr, dc, l):
  if k != best.get((r, c, dr, dc), k): return
  if grid[r][c] == "E":
    if k == end_cost:
      global seen
      seen = seen.union(set(l + [(r, c)]))
    return
  if grid[r + dr][c + dc] != "#":
    dfs(k + 1, r + dr, c + dc, dr, dc, l + [(r, c)])
  if grid[r - dc][c + dr] != "#":
    dfs(k + 1000, r, c, -dc, dr, l + [(r, c)])
  if grid[r + dc][c - dr] != "#":
    dfs(k + 1000, r, c, dc, -dr, l + [(r, c)])


dfs(0, sr, sc, 0, 1, [])

print(f"Part 2: {len(seen)}")

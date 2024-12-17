from re import findall
from math import lcm

WIDTH = 101
HEIGHT = 103

robots = {}
for line in open("input.txt", "r"):
  px, py, vx, vy = map(int, findall(r"-?\d+", line))
  robots[(px, py)] = robots.get((px, py), []) + [(vx, vy)]


def prind_robots(robots):
  for y in range(HEIGHT):
    for x in range(WIDTH):
      l = robots.get((x, y), [])
      if l == []: print(".", end="")
      else: print(len(l), end="")
    print()


###############*###############
#           PART 1            #
###############*###############
def step_robots(robots: dict[tuple[int, int], list[tuple[int, int]]], n=100):
  new_robots = {}
  for (px, py), vs in robots.items():
    for (vx, vy) in vs:
      nx = (px + vx * n) % WIDTH
      ny = (py + vy * n) % HEIGHT
      new_robots[(nx, ny)] = new_robots.get((nx, ny), []) + [(vx, vy)]

  return new_robots


def count_quadrants(robots):
  tl = bl = tr = br = 0
  for (px, py), vs in robots.items():
    if px < WIDTH // 2:
      if py < HEIGHT // 2: tl += len(vs)
      elif py > HEIGHT // 2: bl += len(vs)
    elif px > WIDTH // 2:
      if py < HEIGHT // 2: tr += len(vs)
      elif py > HEIGHT // 2: br += len(vs)
  return tl * bl * tr * br


print("Part 1:", count_quadrants(step_robots(robots)))


###############*###############
#           PART 2            #
###############*###############
def calculate_entropy(robots):
  entropy = 0
  for (px, py), vs in robots.items():
    nn = 0
    for nx, ny in [(px + 1, py), (px - 1, py), (px, py + 1), (px, py - 1)]:
      nn += len(robots.get((nx, ny), []))
    entropy += nn * len(vs)
  return entropy


entropies = []
for i in range(1, lcm(WIDTH, HEIGHT) + 1):
  robots = step_robots(robots, n=1)
  entropies += [(calculate_entropy(robots), i)]

t_tree = max(entropies)[1]
prind_robots(step_robots(robots, n=t_tree))
print(f"Part 2: {t_tree}")

inpt = open("input.txt", "r").read().strip().split("\n\n")


def parse_game(lines):
  a, b, p = lines.split("\n")
  xa, ya = map(int, a[12:].split(", Y+"))
  xb, yb = map(int, b[12:].split(", Y+"))
  xp, yp = map(int, p[9:].split(", Y="))

  return xa, ya, xb, yb, xp, yp


###############*###############
#           PART 1            #
###############*###############


def compute_ab(xa, ya, xb, yb, xp, yp):
  assert (xb * ya - xa * yb) != 0
  b = (xp * ya - yp * xa) / (xb * ya - xa * yb)
  a = (xp - b * xb) / xa

  return a, b


res1 = 0
for lines in inpt:
  a, b = compute_ab(*parse_game(lines))
  if a == int(a) and b == int(b):
    res1 += int(a) * 3 + int(b)

print(f"Part 1: {res1}")
###############*###############
#           PART 2            #
###############*###############

res2 = 0
for lines in inpt:
  *rest, xp, yp = parse_game(lines)
  a, b = compute_ab(*rest, xp + 10000000000000, yp + 10000000000000)
  if a == int(a) and b == int(b):
    res2 += int(a) * 3 + int(b)

print(f"Part 2: {res2}")

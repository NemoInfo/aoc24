from re import findall

inpt = open("input.txt", "r").read().split("\n\n")

###############*###############
#           PART 1            #
###############*###############


def compute_tokens(xa, ya, xb, yb, xp, yp):
  assert (xb * ya - xa * yb) != 0
  b = (xp * ya - yp * xa) / (xb * ya - xa * yb)
  a = (xp - b * xb) / xa

  if a == int(a) and b == int(b):
    return int(a) * 3 + int(b)
  return 0


res1 = 0
for lines in inpt:
  res1 += compute_tokens(*map(int, findall(r"\d+", lines)))

print(f"Part 1: {res1}")
###############*###############
#           PART 2            #
###############*###############

res2 = 0
for lines in inpt:
  *rest, xp, yp = [*map(int, findall(r"\d+", lines))]
  res2 += compute_tokens(*rest, xp + 1e13, yp + 1e13)

print(f"Part 2: {res2}")

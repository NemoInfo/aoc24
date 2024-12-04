import numpy as np

file = open("input.txt", "r")
ws = [line.strip() for line in file.readlines()]

###############*###############
#           PART 1            #
###############*###############
ws = np.array([list(row) for row in ws])
# line
res1 = 0
for row in ws:
  row = "".join(row)
  res1 += row.count("XMAS") + row.count("SAMX")

for row in ws.T:
  row = "".join(row)
  res1 += row.count("XMAS") + row.count("SAMX")

for offset in range(-ws.shape[0] + 1, ws.shape[1]):
  row = "".join(ws.diagonal(offset=offset))
  res1 += row.count("XMAS") + row.count("SAMX")

for offset in range(-ws.shape[0] + 1, ws.shape[1]):
  row = "".join(np.fliplr(ws).diagonal(offset=offset))
  res1 += row.count("XMAS") + row.count("SAMX")

print(f"Part 1: {res1}")
###############*###############
#           PART 2            #
###############*###############
kern = np.array([list(l) for l in ["M.S", ".A.", "M.S"]])

res2 = 0
windows = []
for i in range(ws.shape[0] - kern.shape[0] + 1):
  for j in range(ws.shape[1] - kern.shape[1] + 1):
    window = ws[i:i + 3, j:j + 3].copy()
    window[(0, 1, 1, 2), (1, 0, 2, 1)] = "."
    windows += [window]

windows = np.array(windows)

for k in range(4):
  res2 += len(np.where(np.all(windows == kern, axis=(1, 2)))[0])
  kern = np.rot90(kern)

print(f"Part 2: {res2}")

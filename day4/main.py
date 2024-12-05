import numpy as np

file = open("input.txt", "r")
ws = np.array([list(line.strip()) for line in file.readlines()])

###############*###############
#           PART 1            #
###############*###############
dijs = np.array([[-1] * 3 + [0] * 3 + [1] * 3, [-1, 0, 1] * 3]).T
res1 = 0

for ij in np.argwhere(ws == "X"):
  for dij in dijs:
    nij = ij + dij
    for c in "MAS":
      if np.any(nij >= ws.shape) or np.any(nij < 0) or ws[*nij] != c:
        break
      nij += dij
    else:
      res1 += 1

print(f"Part 1: {res1}")

###############*###############
#           PART 2            #
###############*###############
kern = np.array([list(l) for l in ["M.S", ".A.", "M.S"]])
windows = []
res2 = 0

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

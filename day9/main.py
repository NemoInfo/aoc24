from tqdm import tqdm

###############*###############
#           PART 1            #
###############*###############
disk = []
files = []
is_space = False
i = 0
for c in open("input.txt", "r").read()[:-1]:
  if not is_space:
    if len(files) == i:
      files.append((len(disk), int(c)))
    disk += [i] * int(c)
    i += 1
  else:
    disk += [-1] * int(c)
  is_space = not is_space

tdisk = disk.copy()
i = 0
res1 = 0
while i < len(disk):
  if disk[i] != -1:
    res1 += disk[i] * i
    i += 1
    continue
  while disk[-1] == -1 and len(disk) > i:
    disk.pop()
  disk[i] = disk.pop()
  res1 += disk[i] * i
  i += 1

print(f"Part 1: {res1}")

###############*###############
#           PART 2            #
###############*###############
disk = tdisk.copy()

for j in tqdm(range(len(files) - 1, 0, -1)):
  i = 0
  free = 0
  while i < files[j][0]:
    if disk[i] == -1:
      free += 1
      if free == files[j][1]:
        disk[i - free + 1:i + 1] = [j] * free
        disk[files[j][0]:files[j][0] + free] = [-1] * free
        break
    else:
      free = 0
    i += 1

res2 = 0
for i, c in enumerate(disk):
  if c == -1: continue
  res2 += c * i

print(f"Part 2: {res2}")

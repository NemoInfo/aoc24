from functools import cmp_to_key

file = open("input.txt", "r")

rules, updates = file.read().split("\n\n")
rules = [[*map(int, rule.split("|"))] for rule in rules.splitlines()]
updates = [[*map(int, update.split(","))] for update in updates.splitlines()]

###############*###############
#           PART 1            #
###############*###############
cache = {}
for a, b in rules:
  cache[(a, b)] = -1
  cache[(b, a)] = 1


def is_ordered(update):
  for i in range(len(update)):
    for j in range(i + 1, len(update)):
      if cache.get((update[i], update[j]), -1) == 1:
        return False
  return True


res1 = 0
for update in updates:
  if is_ordered(update):
    res1 += update[len(update) // 2]

print(f"Part 1: {res1}")

###############*###############
#           PART 2            #
###############*###############
res2 = 0
for update in updates:
  if is_ordered(update): continue
  update.sort(key=cmp_to_key(lambda x, y: cache.get((x, y), 0)))
  res2 += update[len(update) // 2]

print(f"Part 2: {res2}")

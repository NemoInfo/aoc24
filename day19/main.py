from functools import cache

pats, _, *targets, _ = open("test.txt").read().splitlines()
pats = set(pats.split(", "))
max_pat_len = max(map(len, pats))

###############*###############
#           PART 1            #
###############*###############


@cache
def possible(target):
  if target == "": return True
  for i in range(min(max_pat_len, len(target)) + 1):
    if target[:i] in pats and possible(target[i:]):
      return True
  return False


print("Part 1:", sum(map(possible, targets)))

###############*###############
#           PART 2            #
###############*###############


@cache
def count(target):
  if target == "": return 1
  res = 0
  for i in range(min(max_pat_len, len(target)) + 1):
    if target[:i] in pats:
      res += count(target[i:])
  return res


print("Part 2:", sum(map(count, targets)))

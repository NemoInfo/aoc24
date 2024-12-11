from functools import cache

stones = [*map(int, open("input.txt", "r").read().split())]

###############*###############
#           PART 1            #
###############*###############


@cache
def blink(stone, n):
  if n == 0: return 1
  if stone == 0: return blink(1, n - 1)
  sstone = str(stone)
  slen = len(sstone)
  if slen % 2 == 0:
    return blink(int(sstone[:slen // 2]), n - 1) + \
        blink(int(sstone[slen // 2:]), n - 1)
  return blink(stone * 2024, n - 1)


res1 = sum(blink(stone, 25) for stone in stones)
print(f"Part 1: {res1}")

###############*###############
#           PART 2            #
###############*###############

res1 = sum(blink(stone, 75) for stone in stones)
print(f"Part 2: {res1}")

import re

file = open("input.txt", "r")
text = file.read()

###############*###############
#           PART 1            #
###############*###############
xs = [[int(a), int(b)]
      for a, b in re.findall(r"mul\(([1-9][0-9]*),([1-9][0-9]*)\)", text)]
res1 = 0
for a, b in xs:
  res1 += a * b

print(f"Part 1: {res1}")

###############*###############
#           PART 2            #
###############*###############
matches = re.findall(r"(mul\(([1-9][0-9]*),([1-9][0-9]*)\)|do\(\)|don't\(\))",
                     text)
dont, res2 = False, 0
for instr, a, b in matches:
  if instr == "don't()": dont = True
  if instr == "do()": dont = False
  if dont or not instr.startswith("mul"): continue
  res2 += int(a) * int(b)

print(f"Part 2: {res2}")

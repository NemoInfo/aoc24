from re import findall

registers, program = open("input.txt").read().split("\n\n")
program = list(map(int, findall(r"\d", program)))

###############*###############
#           PART 1            #
###############*###############
reg = {r: v for r, v in zip("ABC", map(int, findall(r"\d+", registers)))}
reg["I"] = 0
out = []

combo = lambda reg, o: o if o < 4 else reg["ABC"[o - 4]]
ops = [
    lambda reg, o: reg.update({"A": reg["A"] >> combo(reg, o)}),
    lambda reg, o: reg.update({"B": reg["B"] ^ o}),
    lambda reg, o: reg.update({"B": combo(reg, o) % 8}),
    lambda reg, o: reg.update({"I": o - 2}) if reg["A"] != 0 else None,
    lambda reg, _: reg.update({"B": reg["B"] ^ reg["C"]}),
    lambda reg, o: out.append(combo(reg, o) % 8),
    lambda reg, o: reg.update({"B": reg["A"] >> combo(reg, o)}),
    lambda reg, o: reg.update({"C": reg["A"] >> combo(reg, o)}),
]

while reg["I"] < len(program) - 1:
  opid, o = program[reg["I"]:reg["I"] + 2]
  ops[opid](reg, o)
  reg["I"] += 2

res = ",".join(map(str, out))
print("Part 1:", res)
###############*###############
#           PART 2            #
###############*###############


# Program: 2,4,1,3,7,5,0,3,4,3,1,5,5,5,3,0
def find(program, ans):
  if program == []: return ans
  for b in range(8):
    a = ans << 3 | b
    b ^= 3
    c = a >> b
    b ^= c
    b ^= 5
    if b % 8 == program[-1]:
      sub = find(program[:-1], a)
      if sub is not None: return sub


print("Part 2:", find(program, 0))
